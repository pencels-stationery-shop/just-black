import glob, os, sys, argparse
from PIL import Image

tgt_icon_dir = './Icons'

perk_template_path = './perk_template.png'
item_template_path = './item_power_addon_template.png'
offering_template_path = './offering_template.png'

def apply_bg(template_image, src_path, tgt_path):
    # Load the default image
    image = Image.open(src_path)
    try:
        composite = Image.alpha_composite(template_image, image)
        directory = os.path.dirname(tgt_path)
        os.makedirs(directory, exist_ok=True)
        composite.save(tgt_path)
    except ValueError:
        pass

def run(src_icon_dir):
    params = [
        (os.path.join(src_icon_dir, 'Actions'),    os.path.join(tgt_icon_dir, 'Actions'),    '*.png', item_template_path),
        (os.path.join(src_icon_dir, 'Perks'),      os.path.join(tgt_icon_dir, 'Perks'),      '*.png', perk_template_path),
        (os.path.join(src_icon_dir, 'Items'),      os.path.join(tgt_icon_dir, 'Items'),      '*.png', item_template_path),
        (os.path.join(src_icon_dir, 'ItemAddons'), os.path.join(tgt_icon_dir, 'ItemAddons'), '*.png', item_template_path),
        (os.path.join(src_icon_dir, 'Powers'),     os.path.join(tgt_icon_dir, 'Powers'),     '*.png', item_template_path),
        (os.path.join(src_icon_dir, 'Favors'),     os.path.join(tgt_icon_dir, 'Favors'),     '*.png', offering_template_path),
    ]

    for (src_dir, tgt_dir, pattern, template_path) in params:
        print('Processing ' + src_dir + ' -> ' + tgt_dir)

        src_paths = glob.glob(os.path.join(src_dir, '**', pattern), recursive=True)
        template_image = Image.open(template_path)
        for src_path in src_paths:
            print('Processing', src_path, '...', end='')
            tgt_path = os.path.join(tgt_dir, os.path.relpath(src_path, src_dir))
            apply_bg(template_image, src_path, tgt_path)
            print('done.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=sys.argv[0], description='Automatically adds black bg to dbd icons.')
    parser.add_argument('default_icons_dir')
    args = parser.parse_args()
    run(args.default_icons_dir)