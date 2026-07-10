%global tl_name apprends-latex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.02
Release:	%{tl_revision}.1
Summary:	Apprends LaTeX!
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/apprends-latex
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apprends-latex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apprends-latex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Apprends LaTeX! ("Learn LaTeX", in English) is French documentation for
LaTeX beginners.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/doc/latex/apprends-latex
%dir %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/Apprends_LaTeX.pdf
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/Apprends_LaTeX.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/README
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/avance.bib
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/bibliographie-index.bib
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/divers.bib
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/Makefile
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/beamer-themes.pl
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/beamer-titlepage.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/currvita.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/curve-experience.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/curve-extra.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/curve-formation.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/curve-langues.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/curve-methodologies.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/curve-references.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/curve.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/letter.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/moderncv.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/polices.pl
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/scrlttr2.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/seraphin-lampion.jpg
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/slides.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/exemples/tikz.tex
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/graphisme.bib
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/index.ist
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/latex.bib
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/latexmkrc
%doc %{_datadir}/texmf-dist/doc/latex/apprends-latex/typographie.bib
