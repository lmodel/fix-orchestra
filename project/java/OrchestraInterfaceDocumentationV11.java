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
  Text about an element of an interfaces file.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraInterfaceDocumentationV11  {

  private String fixiText;
  private List<OrchestraXmlElement> fixiAny;
  private String fixiLangId;
  private String fixiPurpose;
  private String fixiContentType;


}