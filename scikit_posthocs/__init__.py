__version__ = '0.3.3'

from scikit_posthocs._posthocs \
    import posthoc_conover, posthoc_dunn, posthoc_nemenyi,\
           posthoc_ttest, posthoc_tukey_hsd, posthoc_mannwhitney,\
           posthoc_nemenyi_friedman, posthoc_conover_friedman,\
           posthoc_quade, posthoc_durbin, posthoc_vanwaerden

from scikit_posthocs._plotting \
    import sign_array, sign_plot, sign_table

from scikit_posthocs._outliers \
    import outliers_iqr, outliers_grubbs, outliers_tietjen, outliers_gesd
