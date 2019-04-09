def cigar_party(cigars, is_weekend):
  return cigars >= 40 if is_weekend else 40 <= cigars <= 60
