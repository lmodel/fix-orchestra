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
  Usage specific annotation, optionally with link to an external reference or standard
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InterfaceAppinfo  {

  private URI specUrl;
  private String value;
  private List<String> content;
  private List<String> extraAttributes;
  private String langId;
  private String purpose;


}