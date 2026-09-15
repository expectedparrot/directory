# AISS tutorial mirror

The canonical tutorial is maintained in `expectedparrot/aiss`, under `docs/`.
This copy serves the rendered tutorial while the AISS repository is private.

When updating it, copy these three files from AISS's `docs/` to this directory,
preserving their relative paths:

- `index.html`
- `examples/negotiation_tutorial.py`
- `manual/examples/negotiation.json`

Keep the example and fixture byte-identical. In `index.html`, change the artwork
reference to `assets/aiss-artwork.webp` and use its dimensions (currently
1,280 × 840). Copy the compressed artwork from `../../assets/aiss-artwork.webp`
into this directory's `assets/` folder. See the [artwork notes](../../assets/README.md)
when updating the source image.

Run the Python example from an AISS checkout;
the public tutorial directory is not an installed Python package.
