//Oancea Maria-Nicoleta

void detectFace(){
  scale(4);
  opencv.loadImage(video);
  image(video, 0, 0 );

  Rectangle[] faces = opencv.detect();
  
  for (int i = 0; i < faces.length; i++) {
    noFill();
    stroke(0, 255, 0);
    strokeWeight(3);
    rect(faces[i].x+5, faces[i].y, faces[i].width-10, faces[i].height); 
    distance = (FOCAL_WIDTH * FACE_WIDTH) / faces[i].width;
    
    if ( 4*(faces[i].x + faces[i].width/2) < width/3  && 4*(faces[i].y + faces[i].height/2) < height/2) position = 6;    
    if ( 4*(faces[i].x + faces[i].width/2) > 2*width/3  && 4*(faces[i].y + faces[i].height/2) < height/2) position = 2;
    if ( 4*(faces[i].x + faces[i].width/2) > 2*width/3  && 4*(faces[i].y + faces[i].height/2) >= height/2) position = 3;
    if ( 4*(faces[i].x + faces[i].width/2) < width/3  && 4*(faces[i].y + faces[i].height/2) >= height/2) position = 5;
    if ( 4*(faces[i].x + faces[i].width/2) >= width/3 && 4*(faces[i].x + faces[i].width/2) <= 2*width/3 && 4*(faces[i].y + faces[i].height/2) < height/3) position = 1;
    if ( 4*(faces[i].x + faces[i].width/2) >= width/3 && 4*(faces[i].x + faces[i].width/2) <= 2*width/3 && 4*(faces[i].y + faces[i].height/2) > 2*height/3) position = 4;
    if ( 4*(faces[i].x + faces[i].width/2) >= width/3 && 4*(faces[i].x + faces[i].width/2) <= 2*width/3 && 4*(faces[i].y + faces[i].height/2) >= height/3 && 4*(faces[i].y + faces[i].height/2) <= 2*height/3) position = 0;
  }
  if (faces.length == 0) {
    distance = 0;
    position = 0;
  }
}