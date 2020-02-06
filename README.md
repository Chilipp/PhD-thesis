# PhD-thesis of Philipp S. Sommer

[![LICENSE](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

The source files of my PhD-thesis. The PDF document of the thesis is stored as
[main.pdf](main.pdf). The latex master file is stored in [main.tex](main.tex)
with the chapters from the [Chapters](Chapters) directory.

## Compilation
The latex document requires biber for the bibliography and can be compiled via

```bash
pdflatex main
pdflatex main
biber main
pdflatex main
pdflatex main
```

## The template
This thesis is based on the [Masters/Doctoral Thesis](http://www.latextemplates.com/template/masters-doctoral-thesis)
template that was originally created by Steve R. Gunn, modified into a
template by Sunil Patel and revised by Vel. The source files are saved in
[thesis_1.zip] that is available under the [LPPL v1.3c](http://www.latex-project.org/lppl)
license.

## License
This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
