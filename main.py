#if __name__ == '__main__':
#    init()
#    need_to_work()
#    check_usb_disk()
#    mount_usb_disk()
#    check_dir_tree()
#    move_old_backup()
#    copy_files()
#    umount_usb_disk()

from controller.controller import Controller

if __name__ == '__main__':
    controller = Controller()
    controller.run()
