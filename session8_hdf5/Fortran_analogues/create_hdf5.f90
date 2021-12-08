PROGRAM MAIN
    USE HDF5

    IMPLICIT NONE

    CHARACTER*120 :: filename, dname1, dname2 ! File and dataset names
    CHARACTER(LEN=5) :: aname1 = "month"  ! Attribute name
    CHARACTER(LEN=4) :: aname2 = "year"   ! Attribute name

    ! File and dataset identifiers
    INTEGER(HID_T) :: file_id
    INTEGER(HID_T) :: dset1, dset2, attr1, attr2  
    INTEGER(HID_T) :: dspace1, dspace2
    INTEGER(HID_T) :: aspace1, aspace2  
    INTEGER(HID_T) :: atype1, atype2

    ! Data set dimensions
    INTEGER(HSIZE_T), DIMENSION(1) :: dims1, adims  
    INTEGER(HSIZE_T), DIMENSION(2) :: dims2  
    INTEGER :: drank1, drank2, arank

    INTEGER :: error, i

    ! Data set arrays
    INTEGER :: data1d(100)
    REAL*8  :: data2d(2,2)

    ! Attribute data
    INTEGER :: adata1, adata2   

    filename='test.hdf5'

    ! Define the dimensions and names of our two data sets
    drank1 = 1
    drank2 = 2
    arank  = 1   ! dimension of our attributes

    dims1 = 100
    dims2 = 2
    adims = 1

    dname1 = 'Integers'
    dname2 = 'Reals'

    ! Generate some data
    Do i = 2, 100
	data1d(i) = i
    Enddo

    data1d(1) = 1000

    data2d(1,1) = 2.1
    data2d(2,1) = 3.0
    data2d(1,2) = 55.8
    data2d(2,2) = -73.0001


    adata1 = 7
    adata2 = 2018

    !/////////////////////////////////////
    ! Initialize Fortran Interface
    CALL h5open_f(error)

    !/////////////////////////////////////
    ! Create a new file
    CALL h5fcreate_f(filename, H5F_ACC_TRUNC_F, file_id, error)
    
    ! Create the first dataspace
    CALL h5screate_simple_f(drank1, dims1, dspace1,error)

    ! Create the first dataset
    CALL h5dcreate_f(file_id, dname1, H5T_NATIVE_INTEGER, dspace1, &
       dset1, error)

    ! Write to the dataset
    CALL h5dwrite_f(dset1, H5T_NATIVE_INTEGER, data1d, dims1, error)

    !/////////////////////////////////////////////////////////
    ! Before closing our dataset, we add a couple of attributes
    ! Attribute 1:  month -> 7
    ! Attribute 2:  year -> 2018
    ! Create scalar data space for the attribute.
    !
    CALL h5screate_simple_f(arank, adims, aspace1, error)

    ! Create datatype for the attribute.
    CALL h5tcopy_f(H5T_NATIVE_INTEGER, atype1, error)
    CALL h5tset_size_f(atype1, 4, error)

    ! Create dataset attribute.
    CALL h5acreate_f(dset1, aname1, atype1, aspace1, attr1, error)

    ! Write the attribute data.
    CALL h5awrite_f(attr1, atype1, adata1, adims, error)

    ! Close the attribute.
    CALL h5aclose_f(attr1, error)


    ! Use a similar process for our second attribute
    CALL h5screate_simple_f(arank, adims, aspace2, error)
    CALL h5tcopy_f(H5T_NATIVE_INTEGER, atype2, error)
    CALL h5tset_size_f(atype2, 4, error)
    CALL h5acreate_f(dset1, aname2, atype2, aspace2, attr2, error)
    CALL h5awrite_f(attr2, atype2, adata2, adims, error)
    CALL h5aclose_f(attr2, error)


    !////////////////////////////////////


    ! Close first dataset and free related resources
    CALL h5dclose_f(dset1, error)


    ! Create the second dataspace
    CALL h5screate_simple_f(drank2, dims2, dspace2,error)


    ! Create the second dataset
    CALL h5dcreate_f(file_id, dname2, H5T_NATIVE_DOUBLE, dspace2, &
       dset2, error)

    ! Write to the dataset
    CALL h5dwrite_f(dset2, H5T_NATIVE_DOUBLE, data2d, dims2, error)


    ! Close the second dataset and free related resources
    CALL h5dclose_f(dset2, error)



    ! Close the data spaces.
    CALL h5sclose_f(dspace1, error)
    CALL h5sclose_f(dspace2, error)

    ! Close the file.
    CALL h5fclose_f(file_id, error)

    ! Close FORTRAN interface.
    CALL h5close_f(error)

END PROGRAM MAIN
