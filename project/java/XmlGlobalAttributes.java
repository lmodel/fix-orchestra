package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Container for the global <xs:attribute> declarations defined in xml.xsd. Each attribute here is referenceable from other XSDs via ``ref="xml:<name>"``.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class XmlGlobalAttributes  {

  private String lang;
  private String space;
  private URI base;
  private String id;


}