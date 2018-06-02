//Author Dogaru Narcis George
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

using Emgu.CV;
using Emgu.CV.Structure;

namespace VideoPlayer
{
	public partial class Player : Form
	{
		private Capture capture;
		private int playbackSpeed = 0;
		private Boolean playing = true;
		private Boolean captureNow = false;

		public Player(String fileLocation)
		{
			InitializeComponent();
			StartVideo(fileLocation);
		}

		private void StartVideo(String file)
		{
			capture = new Emgu.CV.Capture(file);
			capture.ImageGrabbed += Capture_ImageGrabbed_b;
			playbackSpeed = (int)capture.GetCaptureProperty(Emgu.CV.CvEnum.CapProp.Fps);
			capture.Start();
		}

		private void Capture_ImageGrabbed_b(object sender, EventArgs e)
		{
			try
			{
				Mat m = new Mat();
				capture.Retrieve(m);
				videoHolder.Image = m.ToImage<Bgr, byte>().Bitmap;
				if(captureNow)
				{
					Bitmap image = m.ToImage<Bgr, byte>().Bitmap;
					String macabrePath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "MacabreVideoPlayer");
					String capturesPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "MacabreVideoPlayer", "Captures");
					String filename = DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

					if(!Directory.Exists(macabrePath)) {
						Directory.CreateDirectory(macabrePath);
					}

					if(!Directory.Exists(capturesPath))
					{
						Directory.CreateDirectory(capturesPath);
					}

					image.Save(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "MacabreVideoPlayer", "Captures", filename), System.Drawing.Imaging.ImageFormat.Jpeg);
					captureNow = false;
					MessageBox.Show("Image saved! " + filename);
				}
				Thread.Sleep(playbackSpeed);
			} catch(Exception)
			{

			}
		}

		private void slowPlayback_Click(object sender, EventArgs e)
		{
			if(playbackSpeed <= 100)
			{
				playbackSpeed += 10;
			} else
			{
				playbackSpeed = 100;
			}
		}

		private void fastPlayback_Click(object sender, EventArgs e)
		{
			if(playbackSpeed >= 1)
			{
				playbackSpeed -= 10;
			} else
			{
				playbackSpeed = 1;
			}
		}

		private void pauseButton_Click(object sender, EventArgs e)
		{
			if (playing)
			{
				if (capture != null)
				{
					capture.Pause();
					playing = false;
					pauseButton.HoverImage = VideoPlayer.Properties.Resources.play_hover;
					pauseButton.Image = VideoPlayer.Properties.Resources.play;
					pauseButton.NormalImage = VideoPlayer.Properties.Resources.play;
				}
			} else
			{
				if (capture != null)
				{
					capture.Start();
					playing = true;
					pauseButton.HoverImage = VideoPlayer.Properties.Resources.pause_hover;
					pauseButton.Image = VideoPlayer.Properties.Resources.pause;
					pauseButton.NormalImage = VideoPlayer.Properties.Resources.pause;
				}
			}
		}

		private void customImageButton1_Click(object sender, EventArgs e)
		{
			captureNow = true;
		}
	}
}
