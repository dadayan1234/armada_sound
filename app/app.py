import reflex as rx
import datetime

# --- Komponen Helper (jika diperlukan nanti) ---
# Contoh: Komponen untuk item layanan
# def service_item(icon: str, title: str, description: str):
#     return rx.hstack(
#         rx.icon(tag=icon, size=24, margin_right="10px"),
#         rx.vstack(
#             rx.text(title, font_weight="bold"),
#             rx.text(description, font_size="0.9em", color="gray.600"),
#             align_items="start",
#         ),
#         spacing="4",
#         align_items="center",
#         padding_y="2",
#     )

# --- State (jika butuh interaktivitas lebih lanjut) ---
# class State(rx.State):
#     pass # Belum ada state yang kompleks untuk landing page sederhana

# --- Halaman Utama (Landing Page) ---
@rx.page(title="ARMADA SOUND - Solusi Sound System Profesional")
def index() -> rx.Component:
    current_year = datetime.date.today().year
    whatsapp_number = "+6282233245208" # Ganti dengan nomor WA Anda
    email_address = "info@armadasound.com" # Ganti dengan email Anda
    phone_number = "+6282233245208" # Ganti dengan nomor telepon Anda

    return rx.vstack(
        # --- Bagian Hero ---
        rx.box(
            rx.vstack(
                # Placeholder Logo
                rx.image(src="/logo_placeholder.png", height="80px", margin_bottom="20px", alt="Logo ARMADA SOUND"),
                rx.heading(
                    "ARMADA SOUND",
                    size="9",
                    color="white",
                    text_align="center",
                ),
                rx.heading(
                    "Solusi Sound System Profesional untuk Setiap Acara Anda",
                    size="6",
                    color="gray.200",
                    text_align="center",
                    margin_top="10px",
                    max_width="700px",
                ),
                rx.text(
                    "Hadirkan kualitas suara jernih dan menggelegar untuk hajatan, konser, pengajian, organ tunggal, dan momen spesial lainnya.",
                    color="gray.300",
                    text_align="center",
                    margin_top="20px",
                    max_width="600px",
                ),
                rx.link(
                    rx.button(
                        "Hubungi Kami Sekarang",
                        size="3",
                        margin_top="30px",
                        color_scheme="blue", # Ganti skema warna sesuai selera
                    ),
                    href=f"https://wa.me/{whatsapp_number.replace('+', '')}?text=Halo%20ARMADA%20SOUND,%20saya%20tertarik%20dengan%20layanan%20sound%20system%20Anda.",
                    is_external=True,
                ),
                spacing="4",
                align="center",
                justify="center",
                padding_x="20px",
                padding_y="80px", # Beri padding vertikal lebih banyak
            ),
            bg="linear-gradient(145deg, #1a237e, #3949ab)", # Contoh gradient biru tua
            width="100%",
        ),

        # --- Bagian Layanan/Keunggulan ---
        rx.vstack(
            rx.heading("Mengapa Memilih ARMADA SOUND?", size="7", margin_bottom="20px"),
            rx.text(
                "Kami berkomitmen memberikan pengalaman audio terbaik dengan dukungan:",
                margin_bottom="30px",
                text_align="center",
                max_width="700px",
            ),
            rx.hstack(
                # Kolom 1
                rx.vstack(
                    rx.icon(tag="check_circle", color="green.500", size=32),
                    rx.text("Peralatan Profesional", font_weight="bold", margin_top="10px"),
                    rx.text("Mixer, Power Amplifier, Speaker & Driver kelas atas.", font_size="0.9em", color="gray.600", text_align="center"),
                    align="center",
                    spacing="2",
                    padding="15px",
                ),
                # Kolom 2
                rx.vstack(
                     rx.icon(tag="settings", color="blue.500", size=32),
                    rx.text("Tim Berpengalaman", font_weight="bold", margin_top="10px"),
                    rx.text("Operator & Sound Engineer handal untuk mixing optimal.", font_size="0.9em", color="gray.600", text_align="center"),
                    align="center",
                    spacing="2",
                    padding="15px",
                ),
                # Kolom 3
                rx.vstack(
                    rx.icon(tag="calendar", color="orange.500", size=32),
                    rx.text("Berbagai Jenis Acara", font_weight="bold", margin_top="10px"),
                    rx.text("Siap menangani hajatan, konser, pengajian, rapat, dll.", font_size="0.9em", color="gray.600", text_align="center"),
                    align="center",
                    spacing="2",
                    padding="15px",
                ),
                spacing="8",
                justify="center",
                flex_wrap="wrap", # Agar responsif di layar kecil
                width="100%",
                max_width="1000px",
            ),
            align="center",
            padding_y="60px",
            padding_x="20px",
            width="100%",
            bg="gray.50", # Latar belakang sedikit berbeda
        ),

        # --- Bagian Jenis Acara yang Dilayani ---
        rx.vstack(
            rx.heading("Kami Melayani Berbagai Jenis Acara", size="7", margin_bottom="30px"),
             rx.text(
                "Percayakan kebutuhan audio Anda kepada kami untuk acara:",
                margin_bottom="30px",
                text_align="center",
                max_width="700px",
            ),
           rx.hstack(
                rx.vstack(
                    rx.text("✓ Hajatan Pernikahan / Khitanan"),
                    rx.text("✓ Konser Musik (Indoor / Outdoor)"),
                    rx.text("✓ Acara Hari Besar Nasional / Keagamaan"),
                    rx.text("✓ Pengajian & Habsyian"),
                    align_items="start",
                ),
                 rx.vstack(
                    rx.text("✓ Organ Tunggal & Akustik"),
                    rx.text("✓ Acara Perusahaan (Gathering, Meeting)"),
                    rx.text("✓ Pameran & Peluncuran Produk"),
                    rx.text("✓ Dan berbagai acara lainnya"),
                     align_items="start",
                 ),
                 spacing="8",
                 justify="center",
                 flex_wrap="wrap",
                 padding_x="20px",
           ),
            align="center",
            padding_y="60px",
            padding_x="20px",
            width="100%",
        ),

        # --- Bagian Galeri (Placeholder) ---
        rx.vstack(
            rx.heading("Galeri Acara Kami", size="7", margin_bottom="20px"),
            rx.text(
                "Lihat bagaimana kami memeriahkan berbagai acara dengan kualitas suara terbaik.",
                margin_bottom="30px",
                text_align="center",
                max_width="700px",
            ),
            rx.hstack(
                # Placeholder untuk 3 gambar
                rx.box(rx.text("Foto Acara 1"), bg="gray.300", height="200px", width="300px", border_radius="md", display="flex", align_items="center", justify_content="center"),
                rx.box(rx.text("Foto Acara 2"), bg="gray.300", height="200px", width="300px", border_radius="md", display="flex", align_items="center", justify_content="center"),
                rx.box(rx.text("Foto Acara 3"), bg="gray.300", height="200px", width="300px", border_radius="md", display="flex", align_items="center", justify_content="center"),
                spacing="6",
                justify="center",
                flex_wrap="wrap", # Agar responsif
            ),
            align="center",
            padding_y="60px",
            padding_x="20px",
            width="100%",
            bg="gray.50",
        ),

        # --- Bagian Testimoni (Placeholder) ---
        rx.vstack(
            rx.heading("Apa Kata Klien Kami?", size="7", margin_bottom="30px"),
            rx.hstack(
                 # Placeholder untuk 2 testimoni
                rx.card(
                    rx.vstack(
                        rx.text('"Soundnya mantap, acara hajatan jadi meriah! Tamu semua puas. Recommended!"', font_style="italic"),
                        rx.text("- Bapak Ahmad, Klien Hajatan", font_weight="bold", font_size="0.9em", margin_top="10px", align_self="flex-end"),
                        align_items="start",
                    ),
                    max_width="400px",
                ),
                 rx.card(
                    rx.vstack(
                        rx.text('"Konser band kami sukses besar berkat sound system dari ARMADA SOUND. Jernih dan nendang!"', font_style="italic"),
                        rx.text("- Vokalis Band XYZ, Klien Konser", font_weight="bold", font_size="0.9em", margin_top="10px", align_self="flex-end"),
                        align_items="start",
                    ),
                     max_width="400px",
                ),
                spacing="6",
                justify="center",
                flex_wrap="wrap",
            ),
            align="center",
            padding_y="60px",
            padding_x="20px",
            width="100%",
        ),

        # --- Bagian Kontak ---
        rx.vstack(
            rx.heading("Siap Membuat Acara Anda Menggema?", size="7", margin_bottom="20px"),
            rx.text(
                "Jangan ragu untuk menghubungi kami untuk konsultasi dan pemesanan:",
                margin_bottom="30px",
                text_align="center",
                max_width="600px",
            ),
            rx.hstack(
                rx.link(
                    rx.hstack(rx.icon(tag="phone"), rx.text("Telepon")),
                    href=f"tel:{phone_number}",
                    is_external=True,
                     _hover={"text_decoration": "none"} # Hilangkan underline saat hover
                ),
                rx.divider(orientation="vertical", height="20px", margin_x="15px"),
                rx.link(
                     rx.hstack(rx.icon(tag="chat"), rx.text("WhatsApp")),
                    href=f"https://wa.me/{whatsapp_number.replace('+', '')}?text=Halo%20ARMADA%20SOUND,%20saya%20tertarik%20dengan%20layanan%20sound%20system%20Anda.",
                    is_external=True,
                     _hover={"text_decoration": "none"}
                ),
                 rx.divider(orientation="vertical", height="20px", margin_x="15px"),
                rx.link(
                     rx.hstack(rx.icon(tag="email"), rx.text("Email")),
                    href=f"mailto:{email_address}",
                     _hover={"text_decoration": "none"}
                ),
                spacing="4",
                justify="center",
                align="center",
            ),
             # Tambahkan info alamat jika perlu
            # rx.text("Alamat: [Alamat Lengkap Armada Sound]", margin_top="20px", font_size="0.9em", color="gray.600"),

            align="center",
            padding_y="60px",
            padding_x="20px",
            width="100%",
            bg="gray.100", # Warna latar sedikit berbeda
        ),

        # --- Footer ---
        rx.box(
            rx.text(
                f"© {current_year} ARMADA SOUND. All Rights Reserved.",
                font_size="0.8em",
                color="gray.500",
                text_align="center",
            ),
            padding_y="30px",
            width="100%",
            bg="gray.900",
            color="white"
        ),

        width="100%",
        spacing="0", # Hapus spasi default antar vstack utama
        align="center",
    )

# --- Konfigurasi Aplikasi ---
app = rx.App(
    theme=rx.theme(
        appearance="light", # Bisa 'light', 'dark', atau 'system'
        accent_color="blue", # Warna aksen utama
        radius="medium" # Sudut elemen (misal: 'none', 'small', 'medium', 'large', 'full')
    )
)
app.add_page(index)
# Tidak perlu compile() lagi di versi Reflex yang lebih baru jika dijalankan dengan `reflex run`