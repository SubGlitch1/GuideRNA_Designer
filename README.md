# GuideRNA_Designer
CRISPR Guide RNA Designer

## Description
This is a simple script which is based on public datasets to design guide RNAs for CRISPR research. 
This tool will return the exons, general info and then finally the Target sequence for the gRNA together with detailed info, any reasons to exclude it (due to e.g. offtargeting or low Azimuth score) and even if 4 independent sources calculate the overall score as decisive or not upon a submission of the geneID.

PS: The geneID doesnt have to be the code name but can also be the 3-5 Letter name

Example run for the gene 'SPIDR' (limited to one gRNA only as it only server as an example) 
```
    "guides": [
        {
            "azimuth": 0.5015460293192063,
            "azimuth_display": "0.502",
            "chr_start": 47279844,
            "cutsite": 47279862,
            "exclude_reason": "",
            "exon": "Exon 2",
            "guide": "UUCCAACUCCUUUUUCUCUG",
            "id": 140551662,
            "offtarget": [
                0,
                0,
                3,
                41,
                369
            ],
            "pam_right": false,
            "pick_order": 1,
            "recommendation": [
                true,
                true,
                true,
                true
            ],
            "target": "TTCCAACTCCTTTTTCTCTG"
        },
```
