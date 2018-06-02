import gab.opencv.*;
//Oancea Maria-Nicoleta

import processing.video.*;
import java.awt.*;
import javax.swing.*;
import processing.core.*;
import processing.serial.*;
import controlP5.*;


void setup() {
  size(1280, 960);
  
  //initialization openCV
  video = new Capture(this, FOCAL_WIDTH, FOCAL_HEIGHT);
  opencv = new OpenCV(this, FOCAL_WIDTH, FOCAL_HEIGHT);
  opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE);   
  video.start();
  
  //initialization serial
  myPort = new Serial(this, "COM3", 9600);
  
  //load image
  img1 = loadImage("data/4wd_1.jpg");
  img2 = loadImage("data/4wd_2.jpg");
  img3 = loadImage("data/4wd_3.jpg");
  img4 = loadImage("data/4wd_4.jpg");
  back = loadImage("data/back.png");
  forward = loadImage("data/forward.png");
  forwardRight = loadImage("data/forward_right.png");
  forwardLeft = loadImage("data/forward_left.png");
  backward = loadImage("data/backward.png");
  backwardRight = loadImage("data/backward_right.png");
  backwardLeft = loadImage("data/backward_left.png");
  stop = loadImage("data/stop.png");
  
  cp5 = new ControlP5(this);
  speedSlider = cp5.addSlider("")
                   .setPosition(width-320 ,5)
                   .setSize(300,50)
                   .setRange(0,255)
                   .setValue(150)
                   .setFont(createFont("Arial", 30))
                   .setVisible(false)
                   ;
  thread = new Thread(new Runnable() {
    @Override
    public void run() {
      while(true) {
        try {
          if (page == 0) myPort.write("000");
          if (page == 1) myPort.write("1" + direction + "" + (int)speedSlider.getValue());
          if (page == 2) myPort.write("2" + position + distance);
          if (page == 3 && !start) myPort.write("300");
          if (page == 3 && start) myPort.write("310");
          Thread.sleep(100);
        } catch(Exception e) {
        }
      }
    }
  });
  
  thread.start();
}

void draw() {
  if (page == 0) home();
  if (page == 1) remoteControl();
  else speedSlider.setVisible(false);
  if (page == 2) faceControl();
  if (page == 3) automatic();
  String val="";
  if ( myPort.available() > 0) val = myPort.readStringUntil('\n');  
  println(val);
}

void captureEvent(Capture c) {
  c.read();
}

void mousePressed(){
  if (page == 0) homeClick();
  if (page == 1) remoteControlClick();
  if (page == 2) faceControlClick();
  if (page == 3) automaticClick();
}