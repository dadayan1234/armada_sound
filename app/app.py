import asyncio
import reflex as rx
import datetime
from typing import Optional

# --- Halaman Utama (Landing Page) ---

BANNER_IMAGES = [
    "/img/foto_1.jpg",
    "/img/foto_2.webp",
    "/img/foto_3.png",
]

# --- State untuk Mengelola Carousel ---
class CarouselState(rx.State):
    current_image_index: int = 0
    auto_play: bool = True

    @rx.var
    def current_bg_image(self) -> str:
        return f"url('{BANNER_IMAGES[self.current_image_index]}')"

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(BANNER_IMAGES)

    def prev_image(self):
        self.current_image_index = (self.current_image_index - 1 + len(BANNER_IMAGES)) % len(BANNER_IMAGES)

    def toggle_auto_play(self):
        self.auto_play = not self.auto_play

    async def auto_play_images(self):
        while True:
            if self.auto_play:
                await asyncio.sleep(3)
                self.next_image()
            else:
                await asyncio.sleep(0.1)

@rx.page(title="ARMADA SOUND - Solusi Sound System Profesional")
def index() -> rx.Component:
    current_year = datetime.date.today().year
    whatsapp_number = "+6282233245208" # Ganti dengan nomor WA Anda
    email_address = "info@armadasound.com" # Ganti dengan email Anda
    phone_number = "+6282233245208" # Ganti dengan nomor telepon Anda

    return rx.vstack(
        # --- Bagian Hero (Carousel) ---
        rx.box(
            # Lapisan Konten (Overlay) dengan Efek Blur
            rx.box(
                rx.vstack(
                    # Placeholder Logo (pastikan path benar jika Anda punya logo)
                    rx.image(src="/img/logo.png", # Ganti jika nama file beda
                             height="200px",
                             margin_bottom="20px",
                             alt="Logo ARMADA SOUND"),
                    rx.heading(
                        "ARMADA SOUND",
                        size="9",
                        color="white", # Pastikan teks kontras dengan background
                        text_align="center",
                        text_shadow="0 1px 3px rgba(0,0,0,0.5)", # Bayangan teks agar lebih mudah dibaca
                    ),
                    rx.heading(
                        "Solusi Sound System Profesional untuk Setiap Acara Anda",
                        size="6",
                        color="white", # Warna lebih terang
                        text_align="center",
                        margin_top="10px",
                        max_width="700px",
                        text_shadow="0 1px 2px rgba(0,0,0,0.5)",
                    ),
                    rx.text(
                        "Hadirkan kualitas suara jernih dan menggelegar untuk hajatan, konser, pengajian, organ tunggal, dan momen spesial lainnya.",
                        color="white", # Warna lebih terang
                        text_align="center",
                        margin_top="20px",
                        max_width="600px",
                        text_shadow="0 1px 2px rgba(0,0,0,0.5)",
                    ),
                    rx.link(
                        rx.button(
                            "Hubungi Kami Sekarang",
                            size="3",
                            margin_top="30px",
                            color_scheme="blue",
                        ),
                        href=f"https://wa.me/{whatsapp_number.replace('+', '')}?text=Halo%20ARMADA%20SOUND,%20saya%20tertarik%20dengan%20layanan%20sound%20system%20Anda.",
                        is_external=True,
                    ),
                    spacing="4",
                    align="center",
                    justify="center",
                    # Beri padding agar konten tidak terlalu mepet tepi
                    padding_x="30px",
                    padding_y="50px",
                ),
                # Styling untuk lapisan konten
                position="relative", # Agar konten tidak terpengaruh posisi absolut tombol
                z_index=1, # Di atas background, di bawah tombol navigasi
                width="100%",
                height="100%",
                display="flex", # Menggunakan flexbox untuk centering vertikal/horizontal
                align_items="center",
                justify_content="center",
                # --- EFEK BLUR & Overlay ---
                background_color="rgba(0, 0, 0, 0.35)", # Warna gelap transparan (sesuaikan opacity)
                backdrop_filter="blur(10px)", # Efek blur untuk background di belakangnya (sesuaikan nilai blur)
                border_radius="inherit", # Mengikuti radius container utama jika ada
                transition="background-image 1s ease-in-out",
            ),

            # Tombol Navigasi Carousel
            # Tombol Previous
            rx.icon_button(
                "chevron-left",
                on_click=CarouselState.prev_image,
                position="absolute",
                left="15px", # Jarak dari kiri
                top="50%", # Posisikan di tengah vertikal
                transform="translateY(-50%)", # Koreksi posisi vertikal
                z_index=2, # Di atas lapisan konten
                color_scheme="gray", # Skema warna tombol
                variant="soft", # Tampilan tombol (soft, ghost, solid, outline)
                size="3", # Ukuran tombol
                border_radius="full", # Buat tombol bulat
                opacity=0.7,
                 _hover={"opacity": 1}
            ),
            # Tombol Next
            rx.icon_button(
                "chevron-right",
                on_click=CarouselState.next_image,
                position="absolute",
                right="15px", # Jarak dari kanan
                top="50%",
                transform="translateY(-50%)",
                z_index=2,
                color_scheme="gray",
                variant="soft",
                size="3",
                border_radius="full",
                opacity=0.7,
                 _hover={"opacity": 1}
            ),

            # Styling
            position="relative",
            width="100%",
            min_height="65vh",
            background_image=CarouselState.current_bg_image,
            background_size="cover",
            background_position="center",
            background_repeat="no-repeat",
            overflow="hidden",
            transition="background-image 1s ease-in-out",
            
            # Event handler
            on_mount=CarouselState.auto_play_images,
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
        
        # --- Bagian Galeri Foto ---
        rx.vstack(
            rx.heading("Galeri Dokumentasi", size="7", margin_bottom="30px"),
            rx.hstack(
                rx.image(
                    src="/img/foto_1.jpg",
                    alt="Dokumentasi acara hajatan dengan ARMADA SOUND",
                    height="200px",
                    width="300px",
                    border_radius="md",
                    object_fit="cover"
                ),
                rx.image(
                    src="/img/foto_2.webp",
                    alt="Dokumentasi konser musik dengan ARMADA SOUND",
                    height="200px",
                    width="300px",
                    border_radius="md",
                    object_fit="cover"
                ),
                rx.image(
                    src="/img/foto_3.png",
                    alt="Dokumentasi pengajian akbar dengan ARMADA SOUND",
                    height="200px",
                    width="300px",
                    border_radius="md",
                    object_fit="cover"
                ),
                spacing="6",
                justify="center",
                flex_wrap="wrap",
                width="100%",
            ),
            align="center",
            padding_y="60px",
            padding_x="20px",
            width="100%",
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
             rx.text(f"© {current_year} ARMADA SOUND. All Rights Reserved.", font_size="0.8em", color="gray.500", text_align="center"),
             padding_y="30px", width="100%", bg="gray.900", color="white"
         ),

        width="100%",
        spacing="0",
        align="center",
    )

# --- Konfigurasi Aplikasi ---
app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="blue",
        radius="medium"
    )
)
app.add_page(index, route="/")