#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;
Mat C;
Mat I;
Mat Ior;
int Cnow =1;
int mousedown=0;

//draw class C on the Ior
void drawI();
//callback function for the main window, "Data I"
void mouse_cb1(int event, int x, int y, int flags, void* param);
//callback function for the "Class C" window
void mouse_cb2(int event, int x, int y, int flags, void* param){
    if(event==CV_EVENT_MOUSEMOVE){
        cout<<(unsigned int)C.data[y*C.size().width+x]<<endl;
    }
}

int main(){

    Ior = imread("../../data/numbers.png", CV_LOAD_IMAGE_COLOR);
    I =Ior.clone();
    C=imread("../../data/numbers.bmp", CV_LOAD_IMAGE_GRAYSCALE);
    if(C.data==NULL){
        C=Mat(I.size(),CV_8UC1,Scalar::all(255));
    }else{
        drawI();
    }
    int key;    
    namedWindow("Data I", CV_WINDOW_AUTOSIZE);
    namedWindow("Class C", CV_WINDOW_AUTOSIZE);
    imshow("Data I", I);
    imshow("Class C", C);
    cvSetMouseCallback("Data I", mouse_cb1,0);
    cvSetMouseCallback("Class C", mouse_cb2,0);
    while (true){
        key=waitKey(0);
        //cout<<(char)key;
        switch ((char)key ){
            case '0': cout<<"class: 0"<<endl; Cnow=0; break;
            case '1': cout<<"class: 1"<<endl; Cnow=1; break;
            case '2': cout<<"class: 2"<<endl; Cnow=2; break;
            case '3': cout<<"class: 3"<<endl; Cnow=3; break;
            case '4': cout<<"class: 4"<<endl; Cnow=4; break;
            case '5': cout<<"class: 5"<<endl; Cnow=5; break;
            case '6': cout<<"class: 6"<<endl; Cnow=6; break;
            case '7': cout<<"class: 7"<<endl; Cnow=7; break;
            case '8': cout<<"class: 8"<<endl; Cnow=8; break;
            case '9': cout<<"class: 9"<<endl; Cnow=9; break;
            case '-': cout<<"class null(256)"<<endl; Cnow=255; break;
            case '=': cout<<"saving"<<endl; imwrite("../data/numbers.bmp",C); break;
            case 27: return 0;
            default: break;
        }
    }
    return 0;
}
////////////////////////////////////////implementation
void drawI(){
    int cmax=C.size().width;
    int rmax=C.size().height;
    cout<<"rmax,cmax:"<<rmax<<","<<cmax;
    unsigned char cr,cg,cb;
    float alpha=0.5f;
    for (int r=0;r<rmax;r++){
        for(int c=0;c<cmax;c++){
            switch ((unsigned int)C.data[r*cmax+c]){
                case 1: cr=0x1f;cg=0x77;cb=0xb4;
                I.data[(r*cmax+c)*3]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3]*alpha + (float)cb*(1.0f-alpha));
                I.data[(r*cmax+c)*3+1]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+1]*alpha + (float)cg*(1.0f-alpha));
                I.data[(r*cmax+c)*3+2]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+2]*alpha + (float)cr*(1.0f-alpha));
                break;
                case 2: cr=0xff;cg=0x7f;cb=0x0e;
                I.data[(r*cmax+c)*3]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3]*alpha + (float)cb*(1.0f-alpha));
                I.data[(r*cmax+c)*3+1]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+1]*alpha + (float)cg*(1.0f-alpha));
                I.data[(r*cmax+c)*3+2]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+2]*alpha + (float)cr*(1.0f-alpha));
                break;
                case 3: cr=0x2c;cg=0xa0;cb=0x2c;
                I.data[(r*cmax+c)*3]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3]*alpha + (float)cb*(1.0f-alpha));
                I.data[(r*cmax+c)*3+1]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+1]*alpha + (float)cg*(1.0f-alpha));
                I.data[(r*cmax+c)*3+2]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+2]*alpha + (float)cr*(1.0f-alpha));
                break;
                case 4: cr=0xd6;cg=0x27;cb=0x28;
                I.data[(r*cmax+c)*3]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3]*alpha + (float)cb*(1.0f-alpha));
                I.data[(r*cmax+c)*3+1]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+1]*alpha + (float)cg*(1.0f-alpha));
                I.data[(r*cmax+c)*3+2]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+2]*alpha + (float)cr*(1.0f-alpha));
                break;
                case 5: cr=0x94;cg=0x67;cb=0xbd;
                I.data[(r*cmax+c)*3]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3]*alpha + (float)cb*(1.0f-alpha));
                I.data[(r*cmax+c)*3+1]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+1]*alpha + (float)cg*(1.0f-alpha));
                I.data[(r*cmax+c)*3+2]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+2]*alpha + (float)cr*(1.0f-alpha));
                break;
                case 6: cr=0x8c;cg=0x56;cb=0x4b;
                I.data[(r*cmax+c)*3]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3]*alpha + (float)cb*(1.0f-alpha));
                I.data[(r*cmax+c)*3+1]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+1]*alpha + (float)cg*(1.0f-alpha));
                I.data[(r*cmax+c)*3+2]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+2]*alpha + (float)cr*(1.0f-alpha));
                break;
                case 7: cr=0xe3;cg=0x77;cb=0xc2;
                I.data[(r*cmax+c)*3]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3]*alpha + (float)cb*(1.0f-alpha));
                I.data[(r*cmax+c)*3+1]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+1]*alpha + (float)cg*(1.0f-alpha));
                I.data[(r*cmax+c)*3+2]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+2]*alpha + (float)cr*(1.0f-alpha));
                break;
                case 8: cr=0x7f;cg=0x7f;cb=0x7f;
                I.data[(r*cmax+c)*3]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3]*alpha + (float)cb*(1.0f-alpha));
                I.data[(r*cmax+c)*3+1]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+1]*alpha + (float)cg*(1.0f-alpha));
                I.data[(r*cmax+c)*3+2]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+2]*alpha + (float)cr*(1.0f-alpha));
                break;
                case 9: cr=0xbc;cg=0xbd;cb=0x22;
                I.data[(r*cmax+c)*3]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3]*alpha + (float)cb*(1.0f-alpha));
                I.data[(r*cmax+c)*3+1]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+1]*alpha + (float)cg*(1.0f-alpha));
                I.data[(r*cmax+c)*3+2]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+2]*alpha + (float)cr*(1.0f-alpha));
                break;
                case 0: cr=0x17;cg=0xbe;cb=0xcf;
                I.data[(r*cmax+c)*3]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3]*alpha + (float)cb*(1.0f-alpha));
                I.data[(r*cmax+c)*3+1]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+1]*alpha + (float)cg*(1.0f-alpha));
                I.data[(r*cmax+c)*3+2]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+2]*alpha + (float)cr*(1.0f-alpha));
                break;
                default:break;
            }

        }
    }
}
void mouse_cb1(int event, int x, int y, int flags, void* param){
    int rsq=16;
    int cmax=C.size().width;
    int rmax=C.size().height;
    unsigned char cr,cg,cb;
    float alpha=0.5f;
    switch (Cnow){
        case 1: cr=0x1f;cg=0x77;cb=0xb4;break;
        case 2: cr=0xff;cg=0x7f;cb=0x0e;break;
        case 3: cr=0x2c;cg=0xa0;cb=0x2c;break;
        case 4: cr=0xd6;cg=0x27;cb=0x28;break;
        case 5: cr=0x94;cg=0x67;cb=0xbd;break;
        case 6: cr=0x8c;cg=0x56;cb=0x4b;break;
        case 7: cr=0xe3;cg=0x77;cb=0xc2;break;
        case 8: cr=0x7f;cg=0x7f;cb=0x7f;break;
        case 9: cr=0xbc;cg=0xbd;cb=0x22;break;
        case 0: cr=0x17;cg=0xbe;cb=0xcf;break;
        default:cr=0xff;cg=0xff;cb=0xff;break;
    }
    if(event==CV_EVENT_LBUTTONDOWN){
        mousedown=1;
        for (int r=max(0,y-20);r<min(rmax,y+20);r++){
            for(int c=max(0,x-20);c<min(cmax,x+20);c++){
                if((pow(c-x,2)+pow(r-y,2))<rsq ){
                    C.data[r*cmax+c]= Cnow;
                    I.data[(r*cmax+c)*3]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3]*alpha + (float)cb*(1.0f-alpha));
                    I.data[(r*cmax+c)*3+1]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+1]*alpha + (float)cg*(1.0f-alpha));
                    I.data[(r*cmax+c)*3+2]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+2]*alpha + (float)cr*(1.0f-alpha));
                }
            }
        }

    }
    if(event==CV_EVENT_LBUTTONUP){
        mousedown=0;
    }
    if(event==CV_EVENT_MOUSEMOVE&&mousedown==1){
        for (int r=max(0,y-20);r<min(rmax,y+20);r++){
            for(int c=max(0,x-20);c<min(cmax,x+20);c++){
                if((pow(c-x,2)+pow(r-y,2))<rsq ){
                    C.data[r*cmax+c]= Cnow;
                    I.data[(r*cmax+c)*3]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3]*alpha + (float)cb*(1.0f-alpha));
                    I.data[(r*cmax+c)*3+1]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+1]*alpha + (float)cg*(1.0f-alpha));
                    I.data[(r*cmax+c)*3+2]=(unsigned char)( (float)Ior.data[(r*cmax+c)*3+2]*alpha + (float)cr*(1.0f-alpha));
                }
            }
        }
    }
    imshow("Data I", I);
    imshow("Class C", C);

}
