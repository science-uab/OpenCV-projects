//Author Dogaru Narcis George
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using Emgu.CV;
using Emgu.CV.Structure;

namespace VideoPlayer
{
	public partial class Camera : Form
	{
		private Capture capture;
		private Boolean capturing = false;
		private Boolean paused = false;
		private Boolean captureNow = false;
		private Boolean detectFace = false;
		private Boolean detectEyes = false;

		public Camera()
		{
			InitializeComponent();
		}

		private void startCamera()
		{
			if (capturing == false)
			{
				capture = new Capture(0);
				capture.ImageGrabbed += Capture_ImageGrabbed_b;
				capture.Start();
				capturing = true;
			}
		}
		private void Capture_ImageGrabbed_b(object sender, EventArgs e)
		{
			try
			{
					Mat m = new Mat();
					capture.Retrieve(m);

					if (detectFace == false)
					{
						cameraHolder.Image = m.ToImage<Bgr, byte>().Bitmap;
					} else
					{
						cameraHolder.Image = faceDetection(m);
					}

					if (captureNow)
					{
						Bitmap image;

						if (detectFace == false)
						{
							image = m.ToImage<Bgr, byte>().Bitmap;
						}
						else
						{
							image = faceDetection(m);
						}

						String macabrePath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "MacabreVideoPlayer");
						String cameraPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "MacabreVideoPlayer", "Camera");
						String filename = "photo_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

						if (!Directory.Exists(macabrePath))
						{
							Directory.CreateDirectory(macabrePath);
						}

						if (!Directory.Exists(cameraPath))
						{
							Directory.CreateDirectory(cameraPath);
						}

						image.Save(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "MacabreVideoPlayer", "Camera", filename), System.Drawing.Imaging.ImageFormat.Jpeg);
						captureNow = false;
						MessageBox.Show("Image saved! " + filename);
						
					}

			} catch(Exception)
			{

			}
		}

		private Bitmap faceDetection(Mat m) {
			try
			{
				String face = Path.GetFullPath(@"../../Face/haarcascade_frontalface_default.xml");
				String eye = Path.GetFullPath(@"../../Face/haarcascade_eye.xml");

				CascadeClassifier cascadeClassifier = new CascadeClassifier(face);
				CascadeClassifier cascadeClEyes = new CascadeClassifier(eye);

				Image<Bgr, byte> img = m.ToImage<Bgr, byte>();
				Image<Gray, byte> imgGray = img.Convert<Gray, byte>().Clone();

				Rectangle[] faces = cascadeClassifier.DetectMultiScale(imgGray, 1.1, 4);
				foreach (Rectangle f in faces)
				{
					img.Draw(f, new Bgr(0, 0, 255), 2);

					if (detectEyes == true)
					{
						imgGray.ROI = f;

						Rectangle[] eyes = cascadeClEyes.DetectMultiScale(imgGray, 1.1, 4);

						foreach (Rectangle e in eyes)
						{
							var ey = e;
							ey.X += f.X;
							ey.Y += f.Y;
							img.Draw(ey, new Bgr(0, 0, 255), 2);
						}
					}
				}

				return img.Bitmap;
			}
			catch (Exception ex)
			{
				Console.Write("ERROR" + ex);
			}
			return null;
		}

		private void pauseButton_Click(object sender, EventArgs e)
		{
			if (capturing)
			{
				if (paused == false)
				{
					capture.Pause();
					paused = true;
				}
				else if (paused == true)
				{
					capture.Start();
					paused = false;
				}
			}
		}

		private void stopButton_Click(object sender, EventArgs e)
		{
			if(capturing == true)
			{
				capturing = false;
				capture.Stop();
				capture = null;
			}
		}

		private void recordButton_Click(object sender, EventArgs e)
		{
			startCamera();
		}

		private void captureImage_Click(object sender, EventArgs e)
		{
			captureNow = true;
		}

		private void faceDetect_Click(object sender, EventArgs e)
		{
			if (detectFace == false)
			{
				detectFace = true;	
				faceDetect.Image = VideoPlayer.Properties.Resources.human_skull;
				faceDetect.HoverImage = VideoPlayer.Properties.Resources.human_skull_hover;
				faceDetect.NormalImage = VideoPlayer.Properties.Resources.human_skull_hover;
			} else
			{
				detectFace = false;
				faceDetect.Image = VideoPlayer.Properties.Resources.human_skull_hover;
				faceDetect.HoverImage = VideoPlayer.Properties.Resources.human_skull;
				faceDetect.NormalImage = VideoPlayer.Properties.Resources.human_skull;
			}
		}

		private void detectEyesButton_Click(object sender, EventArgs e)
		{
			if(detectEyes == false)
			{
				detectEyes = true;
				detectEyesButton.Image = VideoPlayer.Properties.Resources.eye;
				detectEyesButton.HoverImage = VideoPlayer.Properties.Resources.eye_hover;
				detectEyesButton.NormalImage = VideoPlayer.Properties.Resources.eye_hover;
			} else
			{
				detectEyes = false;
				detectEyesButton.Image = VideoPlayer.Properties.Resources.eye_hover;
				detectEyesButton.HoverImage = VideoPlayer.Properties.Resources.eye;
				detectEyesButton.NormalImage = VideoPlayer.Properties.Resources.eye;
			}
		}
	}
}
