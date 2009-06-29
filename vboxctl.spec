Name:      vboxctl
Version:   0.1.0
Release:   1
Summary:   VirtualBox Machines Control init script
Group:     System/Server
URL:       http://stockrt.github.com
Vendor:    Sun VirtualBox
Packager:  Rogério Carvalho Schneider <stockrt@gmail.com>
License:   GPL
BuildArch: noarch
Source:    %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id} -un)
Requires:  VirtualBox >= 2

# Recommended Topdir
%define _topdir %(echo $HOME)/rpmbuild
# So the build does not fail due to unpackaged files or missing doc files:
%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0
# No debug package:
%define debug_package %{nil}

%description
VirtualBox Machines Control init script

Usage: ./vboxctl {start|startall|stop|stopall|poweroff|poweroffall|reset|resetall|open|openall|startvm <vmname>|stopvm <vmname>|poweroffvm <vmname>|resetvm <vmname>|openvm <vmname>|status}

With this init script you will be able to control your VMs with the following
options:

- start
Start all configured VMs in /etc/vbox/vbox.cfg

- startall
Start all VMs

- stop
Stop (grace) all configured VMs in /etc/vbox/vbox.cfg

- stopall
Stop (grace) all running VMs

- poweroff
Power off (force) all configured VMs in /etc/vbox/vbox.cfg

- poweroffall
Power off (force) all running VMs

- reset
Reset (reboot) all configured VMs in /etc/vbox/vbox.cfg

- resetall
Reset (reboot) all running VMs

- open
Open GUI for all configured VMs in /etc/vbox/vbox.cfg

- openall
Open GUI for all running VMs

- startvm <vmname>
Start one specific VM

- stopvm <vmname>
Stop one specifc VM

- poweroffvm <vmname>
Power off one specific VM

- resetvm <vmname>
Reset (reboot) one specific VM

- openvm <vmname>
Open GUI for one specific VM

- status
Show which VMs are running

In order to use this initscript you will need to configure
/etc/vbox/vbox.cfg like this:
 VM_USER="stockrt"
 MACHINES="fedora01 centos01 freebsd7 windows-xp"

%prep
%setup -q -n %{name}

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -m 0755 -d %{buildroot}%{_initrddir}
%{__install} -m 0755 -d %{buildroot}%{_sysconfdir}/vbox
%{__install} -m 0755 %{name} %{buildroot}%{_initrddir}/
%{__install} -m 0644 vbox.cfg %{buildroot}%{_sysconfdir}/vbox/

%files
%defattr(-,root,root,-)
%{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/vbox/vbox.cfg

%clean
%{__rm} -rf %{buildroot}

%post
chkconfig --add vboxctl
chkconfig vboxctl on
echo "Please check %{_sysconfdir}/vbox/vbox.cfg for VM_USER and MACHINES"

%preun

%changelog
* Sun Jun 28 2009 - Rogério Carvalho Schneider <stockrt@gmail.com> - 0.1.0-2
- Reviewd VBoxManage path and priority start/stop defaults

* Sun Jun 21 2009 - Rogério Carvalho Schneider <stockrt@gmail.com> - 0.1.0-1
- Initial packing
