%define snapshot 26c3

Name:		wafp
Version:	0.01
Release:	%mkrel 0.%{snapshot}.2
Summary:	Web Application Finger Printer
License:	GPL
Group:		Networking/Other
URL:		http://www.mytty.org/wafp/
Source:     http://www.mytty.org/wafp/%{name}-%{version}-%{snapshot}.tar.bz2
Patch0:     wafp-0.01-26c3-fhs.patch
Requires:   ruby-sqlite3
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
WAFP is a Web Application Finger Printer written in ruby using a SQLite3 DB.

%prep
%setup -q -n %{name}-%{version}-%{snapshot}
%patch0 -p 1

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/wafp
install -d -m 755 %{buildroot}%{_datadir}/wafp/lib
install -d -m 755 %{buildroot}%{_datadir}/wafp/utils

install -m 755 wafp.rb %{buildroot}%{_bindir}
install -m 644 *.db %{buildroot}%{_datadir}/wafp
install -m 644 lib/* %{buildroot}%{_datadir}/wafp/lib
install -m 755 utils/*.sh %{buildroot}%{_datadir}/wafp/utils

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README CREDITS HOWTO
%{_bindir}/wafp.rb
%{_datadir}/wafp
