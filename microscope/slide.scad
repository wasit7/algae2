tube_lenght=15.0;
r_in = 1.5;
r_out = 3.0;
cover_size=19;
channel_thick=1.0;
support_thick=2.0;
module tube(){

	
}
difference(){
	union(){
		//tubes
		translate([+20,0,tube_lenght/2.0]){
			cylinder(h=tube_lenght,r=r_out,center=true,$fn=360);
		}
 		translate([-20,0,tube_lenght/2.0]){
			cylinder(h=tube_lenght,r=r_out,center=true,$fn=360);
		}		
				
		//support layer
		translate([0,0,support_thick/2.0])cube([60,cover_size,support_thick],center=true);
		
	}
	//tubes
	translate([+20,0,tube_lenght/2.0]){
		cylinder(h=tube_lenght+2*support_thick,r=r_in,center=true,$fn=360);
	}
	translate([-20,0,tube_lenght/2.0]){
		cylinder(h=tube_lenght+2*support_thick,r=r_in,center=true,$fn=360);
	}
	//channel
	translate([0,0,channel_thick/2.0])cube([40+2*r_in,2*r_in,channel_thick],center=true);
	//cover slide
	translate([0,0,channel_thick+(support_thick-channel_thick)/2])cube([cover_size,cover_size,(support_thick-channel_thick)],center=true);
}