dir=1
for file in trdg/fonts/custom/E/*.ttf; do
    python trdg/run.py -c 1 -w 12 -f 128 -l vi -dt dict.txt -ft $file -na 2 --output_dir out/$dir
    dir=$((dir+1))
done

dir=20
for file in trdg/fonts/custom/D/*.ttf; do
    python trdg/run.py -c 1 -w 12 -f 128 -l vi -dt dict.txt -ft $file -na 2 --output_dir out/$dir
    dir=$((dir+1))
done

dir=40
for file in trdg/fonts/custom/D/*.otf; do
    python trdg/run.py -c 1000 -w 12 -f 128 -l vi -dt dict.txt -ft $file -na 2 --output_dir out/$dir
    dir=$((dir+1))
done