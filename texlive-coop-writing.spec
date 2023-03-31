Name:		texlive-coop-writing
Version:	61607
Release:	2
Summary:	Support for Cooperative Writing and editorial comments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/coop-writing
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coop-writing.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coop-writing.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coop-writing.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package for Cooperative Writing supports editorial
comments and gives some extra support for writing and
submitting papers, such as anonymization commands for any
document that involves more than one author or editor. The
general behavior of this package is to provide different ways
of marking your text, for example with comments or to-do-notes,
suggestions to add, remove or change text that can be totally
supressed from the output when desired. Mostly, this can be
easily done using one of the three main option states: editing,
submit, and publish. Users should use the editing state most of
the time. In this state, all markings will appear and
anonymization will be off. When submitting, the submit state
will provide a clean article, without any markings, but
anonymized. It is possible to use the options submit and
noanonymize together. Publish will never anonymize. The goal is
to make the submit and publish documents states minimally
invasive, to avoid any clash with publishers' styles. Commands
were inspired from different packages that do not work together
very well, such as ed, todonotes, and color-edits.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/coop-writing
%{_texmfdistdir}/tex/latex/coop-writing
%doc %{_texmfdistdir}/doc/latex/coop-writing

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
