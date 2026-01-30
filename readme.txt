Created by Andreas Verhoeven (AndreasV or Ave) for use in GANT 3. 



Arguments:

-?, show help
-i <directory>, the input directory containing the PNGs to convert. If not specified the current directory will be used.
-o <directory>, the output directory where the newly created ICOns will be saved to.
-s <size> <bpp>, one of the output/bpp formats in the ICO.
-noconfirm, don't ask the user for confirmation
-silent, no progress output (only errors will be shown)



Example call:

png2ico.exe -i c:\pngs -o c:\icons -s 16 8bpp -s 32 8pp -s 48 32bpp -noconfirm

This will convert all PNGs in c:\pngs to icons and store the icons in c:\icons. Each icon will have the following formats: 16x16 8bpp (256colors), 32x32 8pp (256colors), 48x48 32bpp (a lot of colors, including alpha information [XP only] ). Also, the user won't be asked to confirm the conversion.