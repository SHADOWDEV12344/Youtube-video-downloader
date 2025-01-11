from pytube import YouTube
from moviepy.editor import AudioFileClip
from rich.console import Console
from rich.progress import Progress
from time import sleep
import os

console = Console()

def download_youtube_video(url, download_type):
    try:
        # Create YouTube object
        yt = YouTube(url)
        console.print(f"[bold yellow]Downloading:[/] {yt.title}")
        
        # Progress bar for download
        with Progress() as progress:
            task = progress.add_task("[cyan]Downloading...", total=100)

            if download_type == "mp4":
                # Download video as MP4
                video_stream = yt.streams.get_highest_resolution()
                download_path = video_stream.download()
                for i in range(101):  # Simulated progress
                    progress.update(task, advance=1)
                    sleep(0.01)
                console.print(f"[bold green]Video downloaded successfully as MP4: {download_path}")
            
            elif download_type == "mp3":
                # Download video as MP4 and convert to MP3
                video_stream = yt.streams.filter(only_audio=True).first()
                download_path = video_stream.download()
                for i in range(101):  # Simulated progress
                    progress.update(task, advance=1)
                    sleep(0.01)
                
                # Convert MP4 to MP3
                mp3_path = os.path.splitext(download_path)[0] + ".mp3"
                audio = AudioFileClip(download_path)
                audio.write_audiofile(mp3_path)
                audio.close()
                
                # Remove the original MP4 audio file
                os.remove(download_path)
                console.print(f"[bold green]Audio downloaded and converted successfully as MP3: {mp3_path}")
            
            else:
                console.print("[bold red]Invalid download type. Choose 'mp4' or 'mp3'.")
    except Exception as e:
        console.print(f"[bold red]An error occurred:[/] {e}")

def main():
    console.print("[bold blue]Welcome to YouTube Downloader![/]")
    
    # Animated text input
    with Progress() as progress:
        task = progress.add_task("[yellow]Loading downloader...", total=100)
        for i in range(101):  # Simulated progress
            progress.update(task, advance=1)
            sleep(0.01)
    
    # User input
    youtube_url = console.input("[bold cyan]Enter the YouTube video URL: [/] ").strip()
    download_type = console.input("[bold cyan]Download as (mp3/mp4): [/] ").strip().lower()
    
    # Validate input
    if download_type not in ["mp3", "mp4"]:
        console.print("[bold red]Invalid option! Please choose 'mp3' or 'mp4'.[/]")
        return
    
    # Start download
    download_youtube_video(youtube_url, download_type)

if __name__ == "__main__":
    main()
