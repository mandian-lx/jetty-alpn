%{?_javapackages_macros:%_javapackages_macros}
%global reltag v20170118

Name:           jetty-alpn
Version:        8.1.11
Release:        3.%{reltag}.1
Group:          Development/Java
# alpn-tests also contains EPL and ASL, but is not installed
License:        GPLv2+ with exceptions
Summary:        Jetty implementation of ALPN API
URL:            https://github.com/jetty-project/jetty-alpn
Source0:        https://github.com/jetty-project/%{name}/archive/alpn-project-%{version}.%{reltag}.tar.gz
Patch0:         0001-Unshade-alpn-api.patch
BuildArch:      noarch

BuildRequires:  java-1.8.0-openjdk-headless
Requires:       java-1.8.0-openjdk-headless

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty.alpn:alpn-api)
BuildRequires:  mvn(org.eclipse.jetty:jetty-parent:pom:)

%description
A pure Java(TM) implementation of the Application Layer Protocol
Negotiation TLS Extension


%package        javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-alpn-project-%{version}.%{reltag}

# unshade jetty-alpn-api
%patch0 -p1
%pom_remove_plugin -r :maven-shade-plugin

%pom_remove_plugin -r :maven-enforcer-plugin

%pom_disable_module alpn-tests

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.11-3.v20170118
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.11-2.v20170118
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Michael Simacek <msimacek@redhat.com> - 8.1.11-1.v20170118
- Update to upstream version 8.1.11

* Mon Oct 31 2016 Michael Simacek <msimacek@redhat.com> - 8.1.10-1.v20161026
- Update to upstream version 8.1.10
- Relax JDK requirement

* Fri Sep 23 2016 Michael Simacek <msimacek@redhat.com> - 8.1.9-3.v20160720
- Remove spurious cp

* Fri Sep 23 2016 Michael Simacek <msimacek@redhat.com> - 8.1.9-2.v20160720
- Review fixes

* Wed Sep 21 2016 Michael Simacek <msimacek@redhat.com> - 8.1.9-1.v20160720
- Initial packaging
