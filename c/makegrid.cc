// makegrid.cc
//
// Makes envelope models
//
 
#include <stdio.h>
#include "../h/envelope.h"

//------------------------------------------------------------------------


int main(void)
{
	// first get the parameters of the envelope: helium column and the magnetic field strength 
	double yi, Bfield;
	printf("Enter log10 base column of He layer  (0 to force iron)..."); scanf("%lg",&yi);
	printf("Enter B field in G (0 for unmagnetized)..."); scanf("%lg",&Bfield);

	// first need to set whether to use Potekhin's EOS or conductivities or our own
	Envelope envelope;
	envelope.use_potek_eos_in_He = 0;
	envelope.use_potek_cond_in_He = 1;
	envelope.use_potek_eos_in_Fe = 0;
	envelope.use_potek_cond_in_Fe = 1;
	if (Bfield > 0.0) envelope.use_potek_kff=1;
	else envelope.use_potek_kff = 0;

	// now do the integration
	envelope.make_grid( yi, Bfield );   

	// this writes out the result to the file "out/grid"
	// to use this in the cooling code, it needs to be sorted by column depth
	system("sort -g out/grid > out/grid_sorty");

}

