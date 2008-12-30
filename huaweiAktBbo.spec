#
Summary:	HUAWEI E220 modem activator
Summary(pl.UTF-8):	Aktywator modemu HUAWEI E220
Name:		huaweiAktBbo
Version:	20061211
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.kanoistika.sk/bobovsky/archiv/umts/huaweiAktBbo.c
# Source0-md5:	07341a64e0508aa1ab7eff3d8f9e6672
Source1:	http://www.kanoistika.sk/bobovsky/archiv/umts/huaweie220.txt
# Source1-md5:	c619c39e7b636b9820094964953cf257
URL:		http://www.kanoistika.sk/bobovsky/archiv/umts/
BuildRequires:	libusb-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux kernel detects HUAWEI E220 as CDROM. This program disables this
storag device and allows to use E220 as modem.

%description -l pl.UTF-8
Jądro Linuksa wykrywa HUAWEI E220 jako CDROM. Ten program wyłącza "storage
device" i pozwala korzystać z E220 jako z modemu.

%if 0
%package udev
Summary:	udev rules for huaweiAktBbo
Summary(pl.UTF-8):	Reguły udev dla huaweiAktBbo
Group:		-

%description udev

%description udev -l pl.UTF-8
%endif

%prep
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE1} README.sk.txt

%build

gcc huaweiAktBbo.c -ohuaweiAktBbo -lusb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install huaweiAktBbo $RPM_BUILD_ROOT%{_sbindir}/huaweiAktBbo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.sk.txt
%{_sbindir}/huaweiAktBbo
