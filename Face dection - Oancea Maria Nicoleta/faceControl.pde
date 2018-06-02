//Oancea Maria-Nicoleta

void faceControl(){
  detectFace();
  scale(0.25);
  image(back, 0, 0, 100, 60);
  stroke(#ff0000);
  strokeWeight(10);
  line(0, height/2-5, width/3-5, height/2-5);
  line(2*width/3, height/2-5, width, height/2-5);
  line(width/3, height/3-5, 2*width/3-5, height/3-5);
  line(width/3, 2*height/3-5, 2*width/3-5, 2*height/3-5);
  line(width/3-5, 0, width/3-5, height);
  line(2*width/3-5, 0, 2*width/3-5, height);
}

void faceControlClick(){
  if (mouseX < 100 && mouseY < 60) page = 0;
}