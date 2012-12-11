%define snapshot 26c3

Name:		wafp
Version:	0.01
Release:	%mkrel 0.%{snapshot}.4
Summary:	Web Application Finger Printer
License:	GPL
Group:		Monitoring
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


%changelog
* Thu Jul 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-0.26c3.4mdv2011
+ Revision: 689090
- switch group to monitoring, as other security-related tools

* Thu May 19 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-0.26c3.3
+ Revision: 676144
- more complete FHS patch

* Wed May 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-0.26c3.2
+ Revision: 676083
- fix data files location

* Wed May 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-0.26c3.1
+ Revision: 676001
- import wafp

