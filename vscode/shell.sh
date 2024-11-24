for f in *.*; do
    printf "%s\n" "========== $f";
        head -n 2 "$f" | nl
    done