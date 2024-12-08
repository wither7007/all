for f in *.sh do
    printf "%s\n" "========== $f";
        head -n 2 "$f" | nl
    done
