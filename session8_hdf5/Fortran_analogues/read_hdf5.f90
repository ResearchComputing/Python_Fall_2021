PROGRAM MAIN
    USE HDF5

    IMPLICIT NONE

    CHARACTER*80 :: filename, dname1, dname2 ! File and dataset names

    ! File and dataset identifiers
    INTEGER(HID_T) :: file_id
    INTEGER(HID_T) :: dset1, dset2
    INTEGER(HID_T) :: dspace1, dspace2

    ! Data set dimensions
    INTEGER(HSIZE_T), DIMENSION(1) :: dims1, adims  
    INTEGER(HSIZE_T), DIMENSION(2) :: dims2  
    INTEGER :: drank1, drank2

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

    dims1 = 100
    dims2 = 2

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


    !/////////////////////////////////////
    ! Initialize Fortran Interface
    CALL h5open_f(error)

    !/////////////////////////////////////
    ! Open an existing file
    CALL h5fopen_f(filename, H5F_ACC_RDWR_F, file_id, error)
    
    ! Open the dataset.
    CALL h5dopen_f(file_id, dname1, dset1, error)

    !
    ! Read the dataset.
    !
    CALL h5dread_f(dset1, H5T_NATIVE_INTEGER, data1d, dims1, error)

    write(6,*)'Data Set 1: '
    write(6,*)data1d

    CALL h5dclose_f(dset1,error)


    ! Open and read the second dataset.
    CALL h5dopen_f(file_id, dname2, dset2, error)
    CALL h5dread_f(dset2, H5T_NATIVE_DOUBLE, data2d, dims2, error)

    write(6,*)'Data Set 2: '
    write(6,*)data2d

    CALL h5dclose_f(dset2,error)


    ! Close the file.
    CALL h5fclose_f(file_id, error)

    ! Close FORTRAN interface.
    CALL h5close_f(error)

END PROGRAM MAIN
