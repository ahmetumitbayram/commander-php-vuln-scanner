[TR] Commander v1.0 - PHP Proje Güvenlik Tarayıcısı

Commander v1.0, PHP projelerinde potansiyel güvenlik açıklarını tespit etmek amacıyla geliştirilmiş bir araçtır. Bu araç, belirli tehlikeli işlevleri kullanan ve kullanıcı girişlerini güvenli olmayan şekillerde işleyen yerleri bulmanıza yardımcı olur. Aşağıda, Commander v1.0'ın özellikleri ve nasıl kullanıldığına dair bilgiler bulunmaktadır.

Özellikler:

    PHP projelerindeki güvenlik açıklarını tarar ve raporlar.
    Kullanıcı girişi kaynaklarını ve tehlikeli işlevleri içeren önceden tanımlanmış bir liste kullanır.
    Kirli (güvensiz) değişkenleri izleyerek potansiyel güvenlik açıklarını belirler.
    Dosya yolunu, tehlikeli işlevi, satır numarasını ve ilgili değişkeni içeren raporlar sunar.

Kullanım Kılavuzu:

    Commander v1.0'ı çalıştırdığınızda bir dizin yolu girmeniz istenecektir.
    Tarayıcı, belirtilen dizindeki PHP dosyalarını keşfedecek ve potansiyel güvenlik açıklarını kontrol edecektir.
    Tarayıcı, kullanıcı girişi kaynaklarını içeren satırları bulacak ve bu girişleri işleyen değişkenleri izleyecektir.
    Tehlikeli işlevler içeren satırları kontrol edecek ve ilgili değişkenlerin güvenli olup olmadığını kontrol edecektir.
    Kirli (güvensiz) bir değişken kullanıldığında, Commander v1.0 bu bilgileri bir raporda görüntüleyecektir.
    Raporlar, dosya yolunu, tehlikeli işlevi, satır numarasını ve ilgili değişkeni içerecektir.

Örnek Rapor:
    | /path/to/file.php | shell_exec | 24 | $input_var | VULNERABLE |

Not: Commander v1.0 sadece bir tarayıcıdır ve güvenlik açıklarını tespit etmek için kullanılır. Bulunan güvenlik açıklarını düzeltmek ve projenizi güvence altına almak sizin inisiyatifinizdedir.

############################################################################################################################################################################################################

[EN] Commander v1.0 - PHP Project Security Scanner

Commander v1.0 is a tool developed to detect potential security vulnerabilities in PHP projects. This tool helps you identify places that use specific dangerous functions and handle user inputs in unsafe ways. Below are the features of Commander v1.0 and instructions on how to use it.

Features:

- Scans and reports security vulnerabilities in PHP projects.
- Uses a predefined list of user input sources and dangerous functions.
- Identifies potential security vulnerabilities by tracking tainted (unsafe) variables.
- Provides reports with file paths, dangerous functions, line numbers, and related variables.

User Guide:

- When you run Commander v1.0, you will be prompted to enter a directory path.
- The scanner will discover PHP files in the specified directory and check for potential security vulnerabilities.
- It will locate lines that contain user input sources and track the variables that handle these inputs.
- It will check the lines containing dangerous functions and verify if the associated variables are secure.
- When a tainted (unsafe) variable is used, Commander v1.0 will display this information in a report.
- Reports will include the file path, dangerous function, line number, and related variable.

Example Report:
| /path/to/file.php | shell_exec | 24 | $input_var | VULNERABLE |

Note: Commander v1.0 is merely a scanner and is used to detect security vulnerabilities. It is up to you to fix the identified security vulnerabilities and secure your project.
