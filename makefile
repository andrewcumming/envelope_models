# Makefile for makegrid.cc 

# where to put things
CDIR = c
ODIR = o

# compiler
CC = c++
CFLAGS = -O3 -pipe -lgsl -lgslcblas -lgfortran
FORTRAN = gfortran
FFLAGS = -m64 -O3

# main code
OBJS = $(ODIR)/makegrid.o $(ODIR)/root.o $(ODIR)/vector.o $(ODIR)/odeint.o $(ODIR)/eos.o $(ODIR)/condegin13.o $(ODIR)/eosmag13.o $(ODIR)/eos13.o $(ODIR)/envelope.o

makegrid : $(OBJS)
	$(CC) -o makegrid $(OBJS) $(CFLAGS)

# general rules for everything else
$(ODIR)/%.o: $(CDIR)/%.cc
	$(CC) -c $< -o $@ $(CFLAGS)

$(ODIR)/%.o: $(CDIR)/%.c
	$(CC) -c $< -o $@ $(CFLAGS)

$(ODIR)/%.o: $(CDIR)/%.f
	$(FORTRAN) -c $< -o $@ $(FFLAGS)
	
# use 'make clean' to clean up
clean:
	rm -f $(ODIR)/*.o
