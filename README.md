# DRACH_RBP_predict

A pipeline to predict the RBP for DRACH

# Dependencies

# Work flow

![Alt text](image-1.png)

# Usage

- 1.convert bed file to sequence

  ```
  cd scripts
  python bedToSeq.py -i <path_to_bed_file> -p <int: extra_length_add_to_DRACH> -r <reference_fasta>
  ```

  example use:

  ```
  python bedToSeq.py -i ../example/test.bed -p 5 -r /restricted/projectnb/benwol/jmh/script/ref/human/hg38_111/Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa
  ```

- 2.find the RBP mofit

  ```
  python Motif.py -mr <path_to_motif_library>
  ```

  example use:

  ```
  python Motif.py -mr /restricted/projectnb/casa/bu_brain_rnaseq/hippo_rawdata/circrna/homer/data/knownTFs/known.rna.motifs
  ```

# Todo

- [x] bedToSeq.py
- [x] test bedToSeq.py
- [x] Motif.py
- [x] test Motif.py
- [x] Modify rk.py
- [x] Visualization.js + html
- [ ] Interactive test
- [ ] integrating test
