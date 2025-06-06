def vtx_command(*bytes_):
    """Retourne une séquence de commande Minitel en bytes."""
    return bytes(bytes_)

def write_vtx_file(filename, content_bytes):
    with open(filename, 'wb') as f:
        f.write(content_bytes)

def generate_sample_vtx():
    vtx_data = bytearray()

    # Réinitialisation terminal (ESC @)
    vtx_data += vtx_command(0x1B, 0x40)

    # Effacer l'écran (ESC E)
    vtx_data += vtx_command(0x1B, 0x45)

    # Couleur jaune (ESC Q 43)
    vtx_data += vtx_command(0x1B, 0x51, 0x43)

    # Positionner curseur à ligne 12, colonne 10 (ESC Y + 32 + ligne + 32 + col)
    line, col = 12, 10
    vtx_data += vtx_command(0x1B, 0x59, 0x20 + line, 0x20 + col)

    # Texte
    message = "Bonjour Minitel !"
    vtx_data += message.encode('ascii')

    return vtx_data

# Générer le fichier
vtx_bytes = generate_sample_vtx()
write_vtx_file("exemple.vtx", vtx_bytes)
