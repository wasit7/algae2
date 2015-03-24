tube_lenght=15.0;
r_in = 1.2;
r_out = 2.2;
cover_size=10;
channel_thick=1.0;
support_thick=1.8;
stt=40.0;//space between tube
module tube(){

	
}
difference(){
	union(){
		//tubes
		translate([+0.5*stt,0,tube_lenght/2.0]){
			cylinder(h=tube_lenght,r=r_out,center=true,$fn=360);
		}
 		translate([-0.5*stt,0,tube_lenght/2.0]){
			cylinder(h=tube_lenght,r=r_out,center=true,$fn=360);
		}		
				
		//support layer
		translate([0,0,support_thick/2.0])cube([stt+cover_size,cover_size,support_thick],center=true);
		
	}
	//tubes
	translate([+0.5*stt,0,tube_lenght/2.0]){
		cylinder(h=tube_lenght+2*support_thick,r=r_in,center=true,$fn=360);
	}
	translate([-0.5*stt,0,tube_lenght/2.0]){
		cylinder(h=tube_lenght+2*support_thick,r=r_in,center=true,$fn=360);
	}
	//channel
	translate([0,0,channel_thick/2.0])cube([stt+2*r_in,4*r_in,channel_thick],center=true);
	//cover slide
	translate([0,0,channel_thick+(support_thick-channel_thick)/2])cube([cover_size,4*r_in,(support_thick-channel_thick+1)],center=true);
}