HDF5_INC=$(CURC_HDF5_INC)
HDF5_LIB=$(CURC_HDF5_LIB)

create:
	ifort create_hdf5.f90 -I$(HDF5_INC) -L$(HDF5_LIB) -lhdf5_fortran -o create_hdf5
read:
	ifort read_hdf5.f90 -I$(HDF5_INC) -L$(HDF5_LIB) -lhdf5_fortran -o read_hdf5
groups:
	ifort create_groups.f90 -I$(HDF5_INC) -L$(HDF5_LIB) -lhdf5_fortran -o create_groups
modify:
	ifort modify_groups.f90 -I$(HDF5_INC) -L$(HDF5_LIB) -lhdf5_fortran -o modify_groups
subgroups:
	ifort subgroups.f90 -I$(HDF5_INC) -L$(HDF5_LIB) -lhdf5_fortran -o subgroups
all:
	make create
	make read
	make groups
	make modify
	make subgroups
clean:
	rm -rf create_hdf5
	rm -rf read_hdf5
	rm -rf create_groups
	rm -rf modify_groups
	rm -rf subgroups

