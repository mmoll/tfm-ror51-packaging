# Generated from concurrent-ruby-1.0.5.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name concurrent-ruby

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.5
Release: 4%{?dist}
Summary: Modern concurrency tools for Ruby. Inspired by Erlang, Clojure, Scala, Haskell, F#, C#, Java, and classic concurrency patterns
Group:   Development/Languages
License: MIT
URL:     http://www.concurrent-ruby.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.9.3
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Obsoletes: tfm-rubygem-%{gem_name} < 1:1.0.5-3
Obsoletes: tfm-rubygem(%{gem_name}) < 1:1.0.5-3

%{?scl:Requires: %{?scl_prefix}runtime}

%description
Modern concurrency tools including agents, futures, promises, thread pools,
actors, supervisors, and more.
Inspired by Erlang, Clojure, Go, JavaScript, actors, and classic concurrency
patterns.


%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Mon May 14 2018 Evgeni Golov - 1.0.5-4
- Fix the epoch of the tfm-rubygem-concurrent-ruby obsolete

* Mon May 14 2018 Evgeni Golov - 1.0.5-3
- Obsolete the plain tfm version of this gem, as we moved it to the tfm-ror51 SCL.

* Thu Mar 22 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.5-2
- rebuilt

* Tue Nov 21 2017 Eric D. Helms <ericdhelms@gmail.com> - 1.0.5-1
- Initial package
