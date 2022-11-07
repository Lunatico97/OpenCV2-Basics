#include <iostream>
#include <cmath>
#include <cstdlib>
#include <SDL2/SDL.h>

class Vector2f{
    private:
        float x, y ;
    public:
        // Two-dimensional vector
        Vector2f() {}

        Vector2f(float x1, float y1) : x(0.0f), y(0.0f){
            x = x1 ;
            y = y1 ;
        }

        Vector2f operator = (const Vector2f& vec) {
            this->x = vec.x ;
            this->y = vec.y ;
            return *this ;
        }

        Vector2f operator -= (const Vector2f& vec) {
            this->x -= vec.x ;
            this->y -= vec.y ;
            return *this ;
        }

        // Dot product
        float dot(Vector2f vec){
            return x*vec.getX() + y*vec.getY() ;
        }

        float getX() {return x ;}
        float getY() {return y ;}

        void logs(){
            std::cout << "[" << x << ", " << y << "]" << std::endl ;
        }
} ;

class PerlinNoise{
    private:
        int wrapAroundValue = 256 ; // 0 to 255 for RGB scale
        Vector2f br, bl, tr, tl ;
        int brv, blv, trv, tlv ;
        int pTable[256] ;
    
    public:
        void shuffleArray(int arr[]){
            int index, temp ;
            for(int i = sizeof(arr)/sizeof(arr[0])-1; i > 0; i--){
                index = std::round(std::rand()*(i-1)),
                temp  = arr[i];
                arr[i] = arr[index];
                arr[index] = temp;
            }
        }

        void makePermutation(){
            for(int i = 0; i < wrapAroundValue; i++){
                pTable[i] = i ;
            }
            shuffleArray(pTable);
        }

        Vector2f getUnitVector(int v){
            int h = v % 4 ;
            if(h == 0)
                return Vector2f(1.0, 1.0);
            else if(h == 1)
                return Vector2f(-1.0, 1.0);
            else if(h == 2)
                return Vector2f(-1.0, -1.0);
            else
                return Vector2f(1.0, -1.0);
        }


        float fade(float t){
            return ((6*t - 15)*t + 10)*t*t*t;
        }

        float lerp(float t,float a1,float a2){
            return a1 + t*(a2-a1);
        }

        float generateNoise2d(int x, int y){
            Vector2f point(x, y), localPoint(x % wrapAroundValue, y % wrapAroundValue) ;
            point -= localPoint ;
            x = point.getX() ;
            y = point.getY() ;
            makePermutation() ;

            //Setting up corners 
            tl = Vector2f(x, y) ;
            tr = Vector2f(x + 1.0f, y) ;
            br = Vector2f(x + 1.0f, y + 1.0f) ;
            bl = Vector2f(x, y + 1.0f) ;

            //Setting up permutation values from every corner to interpolate later
            int X = localPoint.getX() ;
            int Y = localPoint.getY() ;
            tlv = pTable[pTable[X]+Y] ;
            trv = pTable[pTable[X-1]+Y] ;
            brv = pTable[pTable[X-1]+Y-1] ;
            blv = pTable[pTable[X]+Y-1] ;

            //Generating the values for each corner
            tlv = tl.dot(getUnitVector(tlv)) ;
            trv = tr.dot(getUnitVector(trv)) ;
            brv = br.dot(getUnitVector(brv)) ;
            blv = bl.dot(getUnitVector(blv)) ;

            //Interpolating between the bounds to get the value
            x = fade(x) ;
            y = fade(y) ;
            return lerp(x, lerp(y, blv, tlv), lerp(y, brv, tlv)) ;
        }
} ;

int main(int argc, char *argv[]){
    std::cout << "Perlin Noise Demo" << std::endl ;
    PerlinNoise noise ;
    
    SDL_Window *window = SDL_CreateWindow("Perlin Noise", 10, 10, 500, 500, 0) ;
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, 0) ;
    SDL_Event event ;
    bool status = true ;

    while(status){
        while(SDL_PollEvent(&event)){
            if(event.type == SDL_QUIT)
                status = false ;
        }

        SDL_RenderClear(renderer) ;

        for(int y = 0; y < 500; y++){
            for(int x = 0; x < 500; x++){
                //Noise2D generally returns a value in the range [-1.0, 1.0]
                float n = noise.generateNoise2d(x*0.3, y*0.3);
                
                //Transform the range to [0.0, 1.0], supposing that the range of Noise2D is [-1.0, 1.0]
                n += 1.0;
                n /= 2.0;
                n = std::round(255*n) ;

                SDL_SetRenderDrawColor(renderer, n, 0, 0, 128) ;
                SDL_RenderDrawPoint(renderer, x, y) ;
            }
        }

        SDL_RenderPresent(renderer) ;
    }

    SDL_Quit() ;
    return 0 ;
}