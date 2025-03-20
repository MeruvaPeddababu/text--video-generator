import torch
import gradio as gr
import tempfile
from diffusers import (
    CogVideoXPipeline, AnimateDiffPipeline, DDIMScheduler
)
from diffusers.utils import export_to_video

# Load the models
cog_pipe = CogVideoXPipeline.from_pretrained("THUDM/CogVideoX-2b", torch_dtype=torch.float16)
cog_pipe.enable_model_cpu_offload()
cog_pipe.enable_sequential_cpu_offload()
cog_pipe.vae.enable_slicing()
cog_pipe.vae.enable_tiling()

adapter = None  # Define motion adapter if required
animate_pipe = AnimateDiffPipeline.from_pretrained(
    "emilianJR/epiCRealism", motion_adapter=adapter, torch_dtype=torch.float16
)
scheduler = DDIMScheduler.from_pretrained(
    "emilianJR/epiCRealism",
    subfolder="scheduler",
    clip_sample=False,
    timestep_spacing="linspace",
    beta_schedule="linear",
    steps_offset=1,
)
animate_pipe.scheduler = scheduler
animate_pipe.enable_vae_slicing()
animate_pipe.enable_model_cpu_offload()

def generate_videos(prompt):
    seed = 42
    generator = torch.manual_seed(seed)

    # Generate video with CogVideoX
    print("Generating video with CogVideoX...")
    cog_video_frames = cog_pipe(
        prompt=prompt,
        num_videos_per_prompt=1,
        num_inference_steps=50,
        num_frames=49,
        guidance_scale=6,
        generator=torch.Generator(device="cuda").manual_seed(seed),
    ).frames[0]

    # Save the video from frames
    cog_video_path = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False).name
    export_to_video(cog_video_frames, cog_video_path)

    # Generate video with AnimateDiff
    print("Generating video with AnimateDiff...")
    animate_output = animate_pipe(
        prompt=prompt,
        num_frames=16,
        guidance_scale=7.5,
        num_inference_steps=50,
        generator=torch.Generator("cpu").manual_seed(seed),
    )
    animate_frames = animate_output.frames[0]

    # Save the AnimateDiff video
    animate_video_path = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False).name
    export_to_video(animate_frames, animate_video_path)

    return cog_video_path, animate_video_path

# Gradio Interface
gr.Interface(
    fn=generate_videos,
    inputs=gr.Textbox(label="Enter Prompt"),
    outputs=[gr.Video(label="CogVideoX Output"), gr.Video(label="AnimateDiff Output")],
    title="AI Video Generation with CogVideoX & AnimateDiff",
    description="Enter a prompt to generate AI videos using CogVideoX and AnimateDiff.",
).launch()
