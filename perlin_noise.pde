int rows, cols ;
int planeW = 1080 ;
int planeH = 720 ;
int dim = 20 ;
float[][] zvalues ;
float freqX, freqY, move = 0.0f ;

void setup(){
  size(640, 480, P3D) ; 
  rows = planeH/dim ;
  cols = planeW/dim ;  
  freqX = 0.15f ;
  zvalues = new float[rows][cols] ;
}

void draw(){
  
  move -= 0.1f ;
  freqY = move ;
  for(int i=0; i<rows; i++){
      freqX = 0.0f ;
      for(int j=0; j<cols; j++){
      zvalues[i][j] = map(noise(freqX, freqY), 0, 1, -100, 100) ;
      freqX += 0.2f ;
    }
    freqY += 0.2f ;
  }
  
  stroke(255) ;
  background(0,20,64) ;
  lights() ;
  fill(20,128,0) ;
  
  translate(-300 ,0,-300) ;
  rotateX(PI/3) ;
  
  for(int i=0; i<rows-1; i++){
    beginShape(TRIANGLE_STRIP) ;
    for(int j=0; j<cols; j++){
      vertex(j*dim, i*dim, zvalues[i][j]) ;
      vertex(j*dim, (i+1)*dim, zvalues[i+1][j]) ;  
    }  
    endShape() ;
  }
  
}
