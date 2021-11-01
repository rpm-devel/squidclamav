%if 0%{?el7}
%define dist .el7
%endif

Name:           squidclamav
Version:        6.16
Release:        1%{?dist}
Summary:        HTTP Antivirus for Squid based on ClamAv and the ICAP protocol

Group:          System Environment/Daemons
License:        GPL
URL:            http://sourceforge.net/projects/squidclamav/
Source0:        http://sourceforge.net/projects/squidclamav/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-httpd.conf
Source2:        clwarn.cgi.ja_JP

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  c-icap-devel c-icap
Requires:       squid c-icap

Packager:       momo-i <webmaster@momo-i.org>
Vendor:         momo-i, http://www.momo-i.org/

%description
SquidClamav v6 is an antivirus for the Squid proxy based on the ICAP
protocol and the awards-winning ClamAv anti-virus toolkit. Using it will
help you securing your home or enterprise network web traffic.
SquidClamav is the most efficient antivirus tool for HTTP traffic
available for free, it is written in C as a c-icap service and can
handle several thousands of connections at once.

%prep
%setup -q

%build
%configure \
	--enable-shared \
	--with-c-icap

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/c-icap
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' | xargs rm

install -D -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -D -m755 %{SOURCE2} $RPM_BUILD_ROOT%{_libexecdir}/%{name}/clwarn.cgi.ja_JP

rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog INSTALL NEWS README
%{!?_licensedir:%global license %%doc}
%license COPYING
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/c-icap/%{name}.conf
%attr(0644,root,root) %{_sysconfdir}/c-icap/%{name}.conf.default
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{_libdir}/c_icap/*.so
%config(noreplace) %{_libexecdir}/%{name}/clwarn.cgi
%{_datadir}/c_icap/templates/squidclamav/*
%{_libexecdir}/%{name}/clwarn.cgi.*
%{_mandir}/man1/%{name}.1.gz

%changelog
* Wed Nov 09 2016 momo-i <webmaster@momo-i.org> - 6.16-1
- Update to 6.16

* Tue Jan 26 2016 momo-i <webmaster@momo-i.org> - 6.15-1
- Update to 6.15

* Mon Nov 09 2015 momo-i <webmaster@momo-i.org> - 6.14-1
- Update to 6.14

* Thu Sep 03 2015 momo-i <webmaster@momo-i.org> - 6.13-7
- Update dist for centos7

* Mon Aug 10 2015 momo-i <webmaster@momo-i.org> - 6.13-6
- Rebuilt for fc23

* Wed Jun 17 2015 momo-i <webmaster@momo-i.org> - 6.13-5
- Update to 6.13

* Thu Apr 16 2015 momo-i <webmaster@momo-i.org> - 6.12-5
- Rebilt for fc22

* Thu Feb  5 2015 momo-i <webmaster@momo-i.org> - 6.12-4
- Update to 6.12
- Change license dir

* Sat Sep 20 2014 momo-i <webmaster@momo-i.org> - 6.11-4
- Update to 6.11

* Tue Nov 19 2013 momo-i <webmaster@momo-i.org> - 6.10-4
- change noreplace for default clwarn.cgi

* Tue Nov 19 2013 momo-i <webmaster@momo-i.org> - 6.10-3
- Add Japanese clwarn.cgi

* Mon Nov 11 2013 momo-i <webmaster@momo-i.org> - 6.10-2
- Add required package

* Wed Oct  9 2013 momo-i <webmaster@momo-i.org> - 6.10-1
- Initial rpm release.
