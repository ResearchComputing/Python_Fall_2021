PROGRAM MAIN
    USE HDF5

    IMPLICIT NONE

    CHARACTER*120 :: filename, dname1, groupname ! File,dataset, group names
    CHARACTER(LEN=5) :: aname1 = "month"  ! Attribute name
    CHARACTER(LEN=4) :: aname2 = "year"   ! Attribute name

    ! File and dataset identifiers
    INTEGER(HID_T) :: file_id, group_id
    INTEGER(HID_T) :: dset1
    INTEGER(HID_T) :: dspace1

    ! Data set dimensions
    INTEGER(HSIZE_T), DIMENSION(1) :: dims1
    INTEGER :: drank1

    INTEGER :: error, i

    ! Data set arrays
    INTEGER :: data1d(10)


    filename='new.hdf5'
    groupname='folder1'

    ! Define the dimensions and name of our data set
    drank1 = 1

    dims1 = 10

    dname1 = 'data_range_1'

    ! Generate some data
    Do i = 1, 10
	data1d(i) = i
    Enddo


    !/////////////////////////////////////
    ! Initialize Fortran Interface
    CALL h5open_f(error)

    !/////////////////////////////////////
    ! Open the file
    CALL h5fopen_f(filename, H5F_ACC_RDWR_F, file_id, error)

    ! Open an existing group
    CALL h5gopen_f(file_id, groupname, group_id, error)

    
    ! Create the dataspace
    CALL h5screate_simple_f(drank1, dims1, dspace1,error)

    ! Create the dataset
    CALL h5dcreate_f(group_id, dname1, H5T_NATIVE_INTEGER, dspace1, &
       dset1, error)

    ! Write the dataset
    CALL h5dwrite_f(dset1, H5T_NATIVE_INTEGER, data1d, dims1, error)

    ! Close the dataspace, data set, and group
    CALL h5sclose_f(dspace1, error)

    CALL h5dclose_f(dset1, error)

    CALL h5gclose_f(group_id,error)

    ! Close the file.
    CALL h5fclose_f(file_id, error)

    ! Close FORTRAN interface.
    CALL h5close_f(error)

END PROGRAM MAIN
