%define	snap	20090525
Summary:	Extra rules and tools for udev
Summary(pl.UTF-8):	Dodatkowe reguły i narzędzia dla udev
Name:		udev-extras
Version:	0
Release:	0.%{snap}.1
License:	GPL v2+
Group:		Base
# git clone --depth 1 git://git.kernel.org/pub/scm/linux/hotplug/udev-extras.git
# cd udev-extras
# git archive master --prefix udev-extras/ | bzip2 > udev-extras-$(date +%Y%m%d).tar.bz2
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	5aa462246e90f0527c78ea9866436f18
URL:		http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html
BuildRequires:	acl-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	gperf
BuildRequires:	libtool
BuildRequires:	libusb-devel
BuildRequires:	libxslt-devel
BuildRequires:	pciutils
BuildRequires:	pkg-config
BuildRequires:	udev-devel >= 141
BuildRequires:	usbutils >= 0.82
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The udev-extras package contains an additional rules and tools to
create and identify devices.

%description -l pl.UTF-8
Pakiet udev-extras zawiera dodatkowe reguły i narzędzia do tworzenia i
identyfikacji urządzeń.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-udev-prefix=/ \
	--with-pci-ids-path=%{_sysconfdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc keymap/README.keymap.txt TODO
%dir %{_datadir}/udev-extras
%attr(755,root,root) %{_datadir}/udev-extras/findkeyboards
%attr(755,root,root) %{_prefix}/lib/ConsoleKit/run-session.d/udev-acl.ck
%attr(755,root,root) /lib/udev/keymap
%attr(755,root,root) /lib/udev/modem-modeswitch
%attr(755,root,root) /lib/udev/pci-db
%attr(755,root,root) /lib/udev/udev-acl
%attr(755,root,root) /lib/udev/usb-db
%attr(755,root,root) /lib/udev/v4l_id
/lib/udev/keymaps
/lib/udev/rules.d/*.rules
%{_mandir}/man8/modem-modeswitch*.8*
