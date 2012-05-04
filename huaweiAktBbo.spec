#
Summary:	HUAWEI E220 modem activator
Summary(pl.UTF-8):	Aktywator modemu HUAWEI E220
Name:		huaweiAktBbo
Version:	20061211
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://www.kanoistika.sk/bobovsky/archiv/umts/%{name}.c
# Source0-md5:	07341a64e0508aa1ab7eff3d8f9e6672
Source1:	http://www.kanoistika.sk/bobovsky/archiv/umts/huaweie220.txt
# Source1-md5:	c619c39e7b636b9820094964953cf257
Source2:	%{name}-udev.rules
URL:		http://www.kanoistika.sk/bobovsky/archiv/umts/
BuildRequires:	libusb-compat-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux kernel detects HUAWEI E220 as CDROM. This program disables this
storag device and allows to use E220 as modem.

%description -l pl.UTF-8
Jądro Linuksa wykrywa HUAWEI E220 jako CDROM. Ten program wyłącza
"storage device" i pozwala korzystać z E220 jako z modemu.

%package udev
Summary:	Udev rules for huaweiAktBbo
Summary(pl.UTF-8):	Reguła udev dla huaweiAktBbo
Group:		Applications

%description udev
Udev rule that executes huaweiAktBbo.

%description udev -l pl.UTF-8
Reguła udev która automatycznie uruchamia wukonuje program
huaweiAktBbo po podłączeniu modemu.

%prep
%setup -q -c -T

%build

%{__cc} %{rpmcppflags} %{rpmcflags} %{rpmldflags} \
	%{SOURCE0} -o %{name} -lusb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/udev/rules.d}

install huaweiAktBbo $RPM_BUILD_ROOT%{_sbindir}/huaweiAktBbo
install %{SOURCE1} README.sk.txt
install %{SOURCE2} $RPM_BUILD_ROOT/etc/udev/rules.d/75-huawei-e220.rules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.sk.txt
%attr(755,root,root) %{_sbindir}/%{name}

%files udev
%defattr(644,root,root,755)
/etc/udev/rules.d/75-huawei-e220.rules
