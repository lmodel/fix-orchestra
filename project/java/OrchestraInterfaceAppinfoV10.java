package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A hint for a particular tool on an element of an interfaces file.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraInterfaceAppinfoV10  {

  private String fixiText;
  private List<OrchestraXmlElement> fixiAny;
  private URI fixiSpecUrl;
  private String fixiLangId;
  private String fixiPurpose;
  private List<OrchestraXmlAttribute> fixiOtherAttributes;


}