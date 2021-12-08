PROGRAM MAIN
    USE HDF5
    IMPLICIT NONE
    Character*120 :: filename
    CHARACTER*10 :: gname1, gname2    ! group names

    INTEGER(HID_T) :: file_id  ! File identifier
    INTEGER(HID_T) :: group1,group2  ! Group Identifiers

    INTEGER :: error

    filename = 'new.hdf5'
    gname1 = 'folder1'
    gname2 = 'folder2'

    ! Open the file
    CALL h5open_f(error)
    CALL h5fcreate_f(filename, H5F_ACC_TRUNC_F, file_id, error)

    ! Create our groups
    CALL h5gcreate_f(file_id, gname1, group1, error)
    CALL h5gclose_f(group1,error)

    CALL h5gcreate_f(file_id, gname2, group2, error)
    CALL h5gclose_f(group2,error)

    ! Close the file and the Fortran interface
    CALL h5fclose_f(file_id, error)
    CALL h5close_f(error)
	

END PROGRAM MAIN
