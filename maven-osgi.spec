%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-osgi
Version:        0.2.0
Release:        6.3
Group:	Development/Java
# Maven-shared defines maven-osgi version as 0.3.0
Epoch:          1
Summary:        Library for Maven-OSGi integration
License:        ASL 2.0
URL:            https://maven.apache.org/shared/maven-osgi
BuildArch:      noarch

# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-osgi-0.2.0 maven-osgi-0.2.0
# find -name *.jar -delete
# tar caf maven-osgi-0.2.0.tar.xz maven-osgi-0.2.0/
Source0:        %{name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute:bndlib)
BuildRequires:  mvn(org.apache.maven.shared:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven:maven-project)

Obsoletes:      maven-shared-osgi < %{epoch}:%{version}-%{release}
Provides:       maven-shared-osgi = %{epoch}:%{version}-%{release}

%description
Library for Maven-OSGi integration.

This is a replacement package for maven-shared-osgi

%package javadoc

Summary:        Javadoc for %{name}
Requires:       jpackage-utils
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q
cp -p %{SOURCE1} LICENSE

# Replace plexus-maven-plugin with plexus-component-metadata
%pom_xpath_set "pom:plugin[pom:artifactId[text()='plexus-maven-plugin']]//pom:goal[text()='descriptor']" generate-metadata
%pom_xpath_set "pom:artifactId[text()='plexus-maven-plugin']" plexus-component-metadata

%build
# Tests depend on binary JARs which were removed from sources
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE


%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-5
- Build with xmvn
- Remove bundled test JARs from sources
- Use POM macros instead of sed

* Wed Feb 20 2013 Tomas Radej <tradej@redhat.com> - 1:0.2.0-4
- Added B/R on maven-shared and maven-local

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Tomas Radej <tradej@redhat.com> - 1:0.2.0-2
- Fixed Provides/Obsoletes

* Mon Jan 07 2013 Tomas Radej <tradej@redhat.com> - 1:0.2.0-1
- Initial version

