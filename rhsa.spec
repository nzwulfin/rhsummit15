Name: rhsa-scap	
Version: 1.0	
Release:	4%{?dist}
Summary: Complete XCCDF and OVAL for all RHSA to date

Group:	System Environment/Base	
License: GPLv2+
URL: http://www.redhat.com/security/data/		
Source0: %{name}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

#BuildRequires:	
#Requires:	

%description
Red Hat publishes XCCDF and OVAL for each RHSA released with corresponding CVE information.  This RPM installs the latest complete file that contains all of the released checks.

OVAL Definitions last updated  2015-04-09T03:17:02

%prep
%setup -n %{name}


%build

%install
rm -rf %{buildroot}
#make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/local/share/xml/scap/rhsa
cp -a com.redhat.rhsa-all.xccdf.xml %{buildroot}/usr/local/share/xml/scap/rhsa/
cp -a com.redhat.rhsa-all.xml %{buildroot}/usr/local/share/xml/scap/rhsa/
cp -a com.redhat.rhsa-20141293.xccdf.xml %{buildroot}/usr/local/share/xml/scap/rhsa/
cp -a com.redhat.rhsa-20141293.xml %{buildroot}/usr/local/share/xml/scap/rhsa/
cp -a com.redhat.rhsa-20141653.xccdf.xml %{buildroot}/usr/local/share/xml/scap/rhsa/
cp -a com.redhat.rhsa-20141653.xml %{buildroot}/usr/local/share/xml/scap/rhsa/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
/usr/local/share/xml/scap/rhsa/com.redhat.rhsa-all.xccdf.xml
/usr/local/share/xml/scap/rhsa/com.redhat.rhsa-all.xml
/usr/local/share/xml/scap/rhsa/com.redhat.rhsa-20141293.xccdf.xml
/usr/local/share/xml/scap/rhsa/com.redhat.rhsa-20141293.xml
/usr/local/share/xml/scap/rhsa/com.redhat.rhsa-20141653.xccdf.xml
/usr/local/share/xml/scap/rhsa/com.redhat.rhsa-20141653.xml


%changelog

