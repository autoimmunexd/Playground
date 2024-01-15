provider "proxmox" {
  pm_api_url      = "https://192.168.1.144:8006/api2/json"
  pm_tls_insecure = true
  pm_user         = "root"
  pm_password     = ""
}

resource "proxmox_vm_qemu" "debian_vm" {
  name        = "debian-vm"
  target_node = "pms"
  memory      = 1024
  cores       = 1
  sockets     = 4
  ide2        = "local:iso/debian-12.0.0-amd64-netinst.iso,media=cdrom"
  bootdisk    = "scsi0"

  network {
    id      = 0
    model   = "virtio"
    bridge  = "vmbr0"
  }

  disk {
    id       = 0
    size     = 20
    storage  = "/var/lib/vz/images/"
    type     = "scsi"
    filename = "debian-vm.qcow2"
  }

  provisioner "remote-exec" {
    inline = [
      "echo 'deb http://deb.debian.org/debian bullseye main' > /etc/apt/sources.list",
      "apt-get update",
      "apt-get install -y debian-base-package"  # Replace with your desired Debian packages
    ]

    connection {
      type        = "ssh"
      user        = "root"
    }
  }
}
